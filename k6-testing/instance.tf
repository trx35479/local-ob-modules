# call load balancer module

data "google_compute_subnetwork" "untrust_subnetwork" {
  project = "${var.host_project_id}"
  name    = "${var.subnetwork}"
  region  = "${var.region}"
}

data "google_compute_subnetwork" "mgmt_subnetwork" {
  project = "${var.host_project_id}"
  name    = "${var.mgmt_subnetwork}"
  region  = "${var.region}"
}

data "google_compute_subnetwork" "palo_subnetwork" {
  project = "${var.host_project_id}"
  name    = "${var.palo_subnetwork}"
  region  = "${var.region}"
}

resource "google_compute_address" "private2" {
  count        = 1
  name         = "untrust-${count.index}"
  address_type = "INTERNAL"
  address      = "${element(var.unstrusted_address, count.index)}"
  project      = "${var.host_project_id}"
  subnetwork   = "${data.google_compute_subnetwork.untrust_subnetwork.self_link}"
}

resource "google_compute_instance" "default" {
  #project = "${var.service_project-id}"

  project      = "${var.host_project_id}"
  count        = 1
  name         = "nginx-${count.index}"
  machine_type = "n1-standard-1"
  zone         = "${var.region}-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-9"
    }
  }

  network_interface {
    subnetwork    = "${data.google_compute_subnetwork.untrust_subnetwork.self_link}"
    network_ip    = "${element(google_compute_address.private2.*.address, count.index)}"
    access_config = {}
  }

  metadata_startup_script = "apt-get install nginx -y"
  tags                    = ["gcp-palo-firewall"]      # this is a critical piece of information as firewall rule uses tag to forward traffic
}

