#!/usr/bin/env bash

API_ID=$(base64 -D env.txt | grep api_id | awk -F= '{print $2}')
API_KEY=$(base64 -D env.txt | grep api_key | awk -F= '{print $2}')
ACCOUNT_ID=$(base64 -D env.txt | grep account_id | awk -F= '{print $2}')
#SITE_ID="15227369"
SITE_ID="55045384"

# check environment variables has been set
# this has to be set as the api will use this value to be allow in api gateway

check_variables() {
	if [[ -z "${API_ID}" ]]; then
		echo "Please set the api_id env"
		exit 1; elif [[ -z "${API_KEY}" ]]; then
			echo "Please set the api_key in env"
			exit 1; elif [[ -z "${ACCOUNT_ID}" ]]; then
				echo "Please set the account_id in env"
	fi
}

check_variables


#curl -d api_id=${API_ID} -d api_key=${API_KEY} -d site_id=${SITE_ID} -d "param=domain_redirect_to_full&value=true" \
#        https://my.incapsula.com/api/prov/v1/sites/configure


curl -X POST -d api_id=${API_ID} -d api_key=${API_KEY} -d site_id=${SITE_ID} https://my.incapsula.com/api/prov/v1/caa/check-compliance