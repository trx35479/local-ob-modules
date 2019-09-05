// create vpc in google

resource "google_compute_network" "vpc_network" {
  name         = "${var.project_name}-vpc"
  project      = "${var.project_id}"
  routing_mode = "GLOBAL"
}

resource "google_compute_subnetwork" "subnetwork" {
  provider         = "google-beta"
  project          = "${var.project_id}"
  count            = "${length(var.subnet)}"
  ip_cidr_range    = "${element(var.subnet, count.index)}"
  name             = "${var.project_name}-subnet"
  network          = "${google_compute_network.vpc_network.self_link}"
  region           = "${var.region}"
  enable_flow_logs = true
}
