# instantiate project here
module "vpc" {
  source = "../common/modules/network"

  region       = "${var.region}"
  project_id   = "rowel-uchi-contino-245704"
  project_name = "my-cluster"
  subnet       = ["10.230.0.0/24", "10.230.3.0/24", "10.230.5.0/24"]
}
