# define the source git repo

variable "service_project_id" {
  default = "anz-cs-palo-np-88de38"
}

variable "region" {
  default = "australia-southeast1"
}

resource "google_sourcerepo_repository" "git" {
  name = "git/local-gcp-modules"
  project = "${var.service_project_id}"
  url = "https://github.com/trx35479/local-gcp-modules.git"
}