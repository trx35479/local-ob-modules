#!/usr/bin/env bash

DOMAIN_NAME="www.example.com"
DOMAIN_IP="130.123.1.24"
API_ID=$(base64 -D env.txt | grep api_id | awk -F= '{print $2}')
API_KEY=$(base64 -D env.txt | grep api_key | awk -F= '{print $2}')
ACCOUNT_ID=$(base64 -D env.txt | grep account_id | awk -F= '{print $2}')

# check environment variables has been set
# this has to be set as the api will use this value to be allow in api gateway

cleanup_log() {
	if [[ -f "output.json" ]]; then
		rm -f output.json temp_file
	fi
}

check_variables() {
	if [[ -z "$API_ID" ]]; then
		echo "Please set the api_id env"
		exit 1; elif [[ -z "$API_KEY" ]]; then
			echo "Please set the api_key in env"
			exit 1; elif [[ -z "$ACCOUNT_ID" ]]; then
				echo "Please set the account_id in env"
	fi
}

# verify the domain format is valid
# domain name format should be www.domain.com

echo ${DOMAIN_NAME} > temp_file

octet_1=$(awk -F. '{print $1}' temp_file)

if [[ "${octet_1}" != "www" ]]; then
    echo "check the first octet of the domain, it should start with www"
    exit 1;
fi

# get the naked domain name

naked_domain_name=$(awk -F. '{print $2"."$3}' temp_file)

# define the site using the api
# https://my.incapsula.com/api/prov/v1/sites/add

check_variables

curl -s -d api_id=${API_ID} -d api_key=${API_KEY} -d account_id=${ACCOUNT_ID} \
     -d "domain=${DOMAIN_NAME}&site_ip=${DOMAIN_IP}&force_ssl=true&log_level=full&send_site_setup_emails=true" \
     https://my.incapsula.com/api/prov/v1/sites/add | tee -a output.json


# get the site_id from the json output | site_id will be used on the next api call

SITE_ID=$(sed 's/{//' output.json | awk -F, '{print $1}' | awk -F: '{print $2}')

# define the site rule
# rule includes changing header values and redirect rule
# https://my.incapsula.com/api/prov/v1/sites/incapRules/add

check_variables

curl -s -d api_id=${API_ID} -d api_key=${API_KEY} -d site_id=${SITE_ID} \
     -d "name=change_host_header&action=RULE_ACTION_REWRITE_HEADER&add_missing=false\
     &to=helloworld.sec.gcpnp.anz&from=${naked_domain_name}&rewrite_name=Host" \
     https://my.incapsula.com/api/prov/v1/sites/incapRules/add

# upload custom certificate and private key (certificate and ky should be base64 encoded)
# https://my.incapsula.com/api/prov/v1/sites/customCertificate/upload

CRT_B64=$(base64 -i certifcate.pem)
KEY_B64=$(base64 -i private.pem)

check_variables

curl -s -d api_id=${API_ID} -d api_key=${API_KEY} -d site_id=${SITE_ID} \
     -d "certificate=${CRT_B64}&private_key=${KEY_B64}" \
     https://my.incapsula.com/api/prov/v1/sites/customCertificate/upload

# create an acl base on ip address
# this is an optional configuration for non-prod deployment to allow testing from development team
# https://my.incapsula.com/api/prov/v1/sites/configure/acl

check_variables
curl -s -d api_id=${API_ID} -d api_key=${API_KEY} -d site_id=${SITE_ID} \
     -d "rule_id=api.acl.whitelisted_ips&ips=1.136.0.0/16" \
     https://my.incapsula.com/api/prov/v1/sites/configure/acl

curl -s -d api_id=${API_ID} -d api_key=${API_KEY} -d site_id=${SITE_ID} \
     -d "rule_id=api.acl.blacklisted_ips&ips=0.0.0.0/0" \
     https://my.incapsula.com/api/prov/v1/sites/configure/acl

# set the location of data storage region
# https://my.incapsula.com/api/prov/v1/sites/data-privacy/region-change

check_variables

curl -s -d api_id=${API_ID} -d api_key=${API_KEY} -d site_id=${SITE_ID} \
     -d "data_storage_region=APAC" \
     https://my.incapsula.com/api/prov/v1/sites/data-privacy/region-change

# clean up directory

cleanup_log