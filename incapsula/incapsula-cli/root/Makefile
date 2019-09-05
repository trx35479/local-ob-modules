.PHONY: build test init shell incap-help incap-list incap-add incap-delete gitTag
.SILENT:
PYTHON_VERSION = 3.5.7
IMAGE_NAME ?= python:$(PYTHON_VERSION)
TAG = $(PYTHON_VERSION)
DOMAIN ?= www.newdomain.com
IP_ADDRESS ?= 192.34.65.78
FORCE_SSL ?=true
CERTIFICATE = ./ssl/certificate.crt
PRIVATE_KEY = ./ssl/certifacate.key

build:
	docker build -t $(IMAGE_NAME) .

test:
	docker run --rm -it --entrypoint="python3" \
	           $(IMAGE_NAME) --version

init:
	export SITE_ID=$(cat env.txt | grep site_id | awk -F= '{print $2}')

incap-help:
	docker run --rm -it --entrypoint="python3" \
	           -v $(shell pwd)/src/:/root/ -w /root/ $(IMAGE_NAME) incap.py site delcert --help

incap-list:
	docker run --rm -it --entrypoint="python3" \
	           -v $(shell pwd)/src/:/root/ -w /root/ $(IMAGE_NAME) incap.py site add_incaprule --help \
               --account_id=${ACCOUNT_ID} \
               --api_id=${API_ID} \
               --api_key=${API_KEY}

incap-add:
	docker run --rm -it --entrypoint="python3" \
               -v $(shell pwd)/src/:/root/ -w /root/ $(IMAGE_NAME) incap.py site add  $(DOMAIN) \
               --site_ip=$(IP_ADDRESS) \
               --force_ssl=$(FORCE_SSL) \
               --account_id=${ACCOUNT_ID} \
               --api_id=${API_ID} \
               --api_key=${API_KEY}

incap-delete:
	@echo "Run the make incap-list to get the site ID and export site id - 'export SITE_ID=xxxxx'"
	docker run --rm -it --entrypoint="python3" \
               -v $(shell pwd)/src/:/root/ -w /root/ $(IMAGE_NAME) incap.py site delete ${SITE_ID} \
               --api_id=${API_ID} \
               --api_key=${API_KEY}

incap-upcert:
	docker run --rm -it -v --entrypoint="python3" \
               -v $(shell pwd)/src:/root/ -w /root/ $(IMAGE_NAME) incap.py site upcert certificate.crt ${SITE_ID} \
               --private_key="certificate.key" \
               --api_id=${API_ID} \
               --api_key=${API_KEY}

incap-delcert:
	docker run --rm -it --entrypoint="python3" \
               -v $(shell pwd)/src/:/root/ -w /root/ $(IMAGE_NAME) incap.py site delcert ${SITE_ID} \
               --api_id=${API_ID} \
               --api_key=${API_KEY}

gitTag:
	-git tag -d $(TAG)
	-git push origin :refs/tags/$(TAG)
	git tag $(TAG)
	git push origin $(TAG)
