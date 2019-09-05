# output selflink

output "vpc" {
  value = "${google_compute_network.vpc_network.self_link}"
}

output "subnet" {
  value = "${google_compute_subnetwork.subnetwork.*.self_link}"
}
