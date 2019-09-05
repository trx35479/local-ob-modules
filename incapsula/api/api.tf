# Upload the certificate - a workaround since resource for upload is not yet available
data "template_file" "format" {
  template = "${file("templates/upload_cert.tpl")}"

  vars {
    API_ID      = "${var.API_ID}"
    API_KEY     = "${var.API_KEY}"
    SITE_ID     = "${incapsula_site.site.id}"
    endpoint    = "${var.endpoint}/sites/customCertificate/upload"
    certificate = "${base64encode(file(var.certificate))}"
    private_key = "${base64encode(file(var.private_key))}"
  }
}

resource "null_resource" "execute" {
  triggers {
    template_rendered = "${data.template_file.format.id}"
  }

  provisioner "local-exec" {
    command = "echo '${data.template_file.format.rendered}' | sh -"
  }

  depends_on = ["incapsula_site.site"]
}

data "template_file" "validation" {
  template = "${file("templates/validation.tpl")}"

  vars {
    API_ID      = "${var.API_ID}"
    API_KEY     = "${var.API_KEY}"
    SITE_ID     = "${incapsula_site.site.id}"
    endpoint    = "${var.endpoint}/sites/configure"
  }
}

resource "null_resource" "apply_validation" {
  triggers {
    template_rendered = "${data.template_file.validation.id}"
  }

  provisioner "local-exec" {
    command = "echo '${data.template_file.validation.rendered}' | sh -"
  }

  depends_on = ["incapsula_site.site", "null_resource.execute"]
}

# Use curl to oher parameters not supportd by provider
resource "null_resource" "curl" {
  triggers {
    site_id = "${incapsula_site.site.id}"
  }

  provisioner "local-exec" {
    command = "curl -s --data 'api_id=${var.API_ID}&api_key=${var.API_KEY}&site_id=${incapsula_site.site.id}&rule_id=api.threats.cross_site_scripting&security_rule_action=api.threats.action.block_request' ${var.endpoint}"
  }
}