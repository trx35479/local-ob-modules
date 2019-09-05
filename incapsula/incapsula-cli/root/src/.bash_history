ls -l
cd /root/
ls -lrt
pwd
exit
ls -la
exit
ls -l
python3 incap.py site list
export ACCOUNT_ID="1284650"
export API_ID="32071"
export API_KEY="1b033a13-c10a-4d6b-a932-876007e55b9d"
python3 incap.py site list
python3 incap.py site list --api_key=32071
python3 incap.py site list --api_key=1b033a13-c10a-4d6b-a932-876007e55b9d
python3 incap.py site list --api_key=1b033a13-c10a-4d6b-a932-876007e55b9d --api_id=32071
python3 incap.py site list --api_key=1b033a13-c10a-4d6b-a932-876007e55b9d --api_id=32071 --account_id=1284650
python3 incap.py site upcert certificate.crt --private_key=certificate.key --api_key=1b033a13-c10a-4d6b-a932-876007e55b9d --api_id=32071 --account_id=1284650
python3 incap.py site upcert certificate.crt 40979118 --private_key=certificate.key --api_key=1b033a13-c10a-4d6b-a932-876007e55b9d --api_id=32071 --account_id=1284650
python3 incap.py site upcert certificate.crt 40979118 --private_key=certificate.key --api_key=1b033a13-c10a-4d6b-a932-876007e55b9d --api_id=32071
python3 incap.py site upcert --list
python3 incap.py site upcert --list --api_key=1b033a13-c10a-4d6b-a932-876007e55b9d --api_id=32071
python3 incap.py site upcert --help --api_key=1b033a13-c10a-4d6b-a932-876007e55b9d --api_id=32071
python3 incap.py site upcert certificate.crt 40979118 --private_key=certificate.key --api_key=1b033a13-c10a-4d6b-a932-876007e55b9d --api_id=32071 --passphrase=pass
python3 incap.py site upcert certificate.crt 40979118 --private_key=certificate.key --api_key=1b033a13-c10a-4d6b-a932-876007e55b9d --api_id=32071 --passphrase=password
exit
python3 incap.py site upcert certificate.crt 40979118 --private_key=certificate.key --api_key=1b033a13-c10a-4d6b-a932-876007e55b9d --api_id=32071
python3 incap.py site upcert certificate.crt 40979118 --private_key=certificate.key --api_key=1b033a13-c10a-4d6b-a932-876007e55b9d --api_id=32071 --passphrase=password
python3 incap.py site upcert certificate.crt 40979118 --private_key=certificate.key --api_key=1b033a13-c10a-4d6b-a932-876007e55b9d --api_id=32071 --passphrase=""
python3 incap.py site upcert certificate.crt 40979118 --private_key=certificate.key --api_key=1b033a13-c10a-4d6b-a932-876007e55b9d --api_id=32071
ls -lrt
exit
ls -lrt
exit
ls -l
python3 incap.py site upcert server.pem 55045384 --private_key=private_key.pem --api_key=1b033a13-c10a-4d6b-a932-876007e55b9d --api_id=32071 --passphrase="password"
ls -lrt
ls -l /etc/ssl/
cd /etc/ssl/
ls -lrt
ls -l certs/
vi certs/nginx-selfsigned.crt
ls -lrt
ls -l
exit
ls -lrt
export ACCOUNT_ID="1284650"
export API_ID="32071"
export API_KEY="1b033a13-c10a-4d6b-a932-876007e55b9d"
ls -lrt
python3 incap.py site list
python3 incap.py site list --api_key=${API_KEY} --api_id=${API_ID} 
python3 incap.py site list --api_key=${API_KEY} --api_id=${API_ID} --account_id=${ACCOUNT_ID}
python3 incap.py site --help --api_key=${API_KEY} --api_id=${API_ID} --account_id=${ACCOUNT_ID}
python3 incap.py site add --help --api_key=${API_KEY} --api_id=${API_ID} --account_id=${ACCOUNT_ID}
python3 incap.py site --help --api_key=${API_KEY} --api_id=${API_ID} --account_id=${ACCOUNT_ID}
python3 incap.py site list_incaprule --api_key=${API_KEY} --api_id=${API_ID} --account_id=${ACCOUNT_ID}
python3 incap.py site list_incaprule --api_key=${API_KEY} --api_id=${API_ID} --account_id=${ACCOUNT_ID} --site_id=55045384
python3 incap.py site list_incaprule 55045384 --api_key=${API_KEY} --api_id=${API_ID} --account_id=${ACCOUNT_ID} 
python3 incap.py site list_incaprule 55045384 --api_key=${API_KEY} --api_id=${API_ID}
python incap.py site add_incaprule --help
python incap.py site add_incaprule 40979118 --to="helloworld.sec.gcpnp.anz" --from="api-np.anz" --name="change_host_header" --rewrite_name="Host" --allow_caching=false                                             --add_missing=false --filter="" --action=RULE_ACTION_REWRITE_HEADER                                             --api_key=${API_KEY} --api_id=${API_ID}
python incap.py site add_incaprule 40979118 --to="helloworld.sec.gcpnp.anz" --from="api-np.anz" --name="change_host_header" --rewrite_name="Host" --allow_caching=false --add_missing=false --filter="" --action=RULE_ACTION_REWRITE_HEADER --api_key=${API_KEY} --api_id=${API_ID}
python incap.py site add_incaprule 40979118 --to="helloworld.sec.gcpnp.anz" --from="api-np.anz" --name="test_change_host_header" --rewrite_name="Host" --add_missing=false --filter="" --action=RULE_ACTION_REWRITE_HEADER --api_key=${API_KEY} --api_id=${API_ID}
python incap.py site list
python incap.py site list --api_id${API_ID} -api_key=${API_KEY} --api_account=${ACCOUNT_ID}
python incap.py site list --api_id=${API_ID} -api_key=${API_KEY} --api_account=${ACCOUNT_ID}
python incap.py site list --api_id=${API_ID} -api_key=${API_KEY} --api_account=${ACCOUNT_ID}
python incap.py site list --api_key=${API_KEY} --api_id=${API_ID} --api_account=${ACCOUNT_ID}
python incap.py site list --api_key=${API_KEY} --api_id=${API_ID}
python incap.py site list --api_key=${API_KEY} --api_id=${API_ID}
python incap.py site list --api_key=${API_KEY} --api_id=${API_ID} --api_account=${ACCOUNT_ID}
python incap.py site list --api_key=${API_KEY} --api_id=${API_ID} --account_id=${ACCOUNT_ID}
python incap.py site delete --help
python incap.py site delete 40979118 --help
python incap.py site delete 40979118 --api_key=${API_KEY} --api_id=${API_ID}
python incap.py site delete 40979118 --api_key=${API_KEY} --api_id=${API_ID}
python incap.py site add www.domain.com --site_ip=35.45.65.43 --force_ssl=true --log_level=full --send_site_setup_emails=true --api_key=${API_KEY} --api_id=${API_ID} --account_id=${ACCOUNT_ID} > domain.txt
ls -l
cat domain.txt 
cat domain.txt | grep ID
cat domain.txt | grep ID | awk -F: '{$print $3}'
cat domain.txt | grep ID | awk -F: '{print $3}'
SITE_ID=$(cat domain.txt | grep ID | awk -F: '{print $3}') |  python incap.py site delete $SITE_ID --api_key=${API_KEY} --api_id=${API_ID}
SITE_ID=$(cat domain.txt | grep ID | awk -F: '{print $3}') && python incap.py site delete $SITE_ID --api_key=${API_KEY} --api_id=${API_ID}
ls -lrt
rm -f domain.txt 
python incap.py site add www.domain.com --site_ip=35.45.65.43 --force_ssl=true --log_level=full --send_site_setup_emails=true --api_key=${API_KEY} --api_id=${API_ID} --account_id=${ACCOUNT_ID} > site_creation.txt
SITE_ID=$(cat site_creation.txt | grep ID | awk -F: '{print $3}') && python incap.py site add_incaprule $SITE_ID --to="helloworld.sec.gcpnp.anz" --from="api-np.anz" --name="test_change_host_header" --rewrite_name="Host" --add_missing=false --filter="" --action=RULE_ACTION_REWRITE_HEADER --api_key=${API_KEY} --api_id=${API_ID}
python incap.py site --help
awk
ls -l
man awk
cat /usr/bin/
ls -l /usr/bin/
pwd
ls -lrt
cat site_creation.txt 
awk -F= '{print $3}' site_creation.txt 
awk -F: '{print $3}' site_creation.txt 
ls -l
python incap.py site --help
python incap.py site whitelist --help
SITE_ID=$(cat site_creation.txt | awk -F: '${print $3}' && python incap.py site whitelist $SITE_ID --ips=10.0.0.0/24,30.0.0.0/24 --api_key=${API_KEY} --api_id=${API_ID} 




SITE_ID=$(cat site_creation.txt | awk -F: '${print $3}') && python incap.py site whitelist $SITE_ID --ips=10.0.0.0/24,30.0.0.0/24 --api_key=${API_KEY} --api_id=${API_ID} 
SITE_ID=$(cat site_creation.txt | awk -F: '{print $3}') && python incap.py site whitelist $SITE_ID --ips=10.0.0.0/24,30.0.0.0/24 --api_key=${API_KEY} --api_id=${API_ID} 
SITE_ID=$(cat site_creation.txt | awk -F: '{print $3}') && python incap.py site whitelist 188599 $SITE_ID --ips=10.0.0.0/24,30.0.0.0/24 --api_key=${API_KEY} --api_id=${API_ID} 
SITE_ID=$(cat site_creation.txt | awk -F: '{print $3}') && python incap.py site whitelist 188599 $SITE_ID --ips=10.0.0.0/24,30.0.0.0/24 --api_key=${API_KEY} --api_id=${API_ID} 
python incap.py site whitelist --help
python incap.py site whitelist list
cat site_creation.txt 
python incap.py site whitelist 35473495
python incap.py site whitelist 188599 35473495
python incap.py site whitelist 188599 35473495
python incap.py site whitelist 188599 35473495 --api_key=${API_KEY} --api_id=${API_ID}
python incap.py --help
python incap.py account --help
python incap.py account list --api_key=${API_KEY} --api_id=${API_ID}
python incap.py account list --api_key=${API_KEY} --api_id=${API_ID} --account_id=${ACCOUNT_IF\\\
python incap.py config --help
python incap.py site --help
python incap.py site acl --help
python incap.py site --help
python incap.py site security --help
python incap.py site list --api_key=${API_KEY} --api_id=${API_ID}
python incap.py site list --api_key=${API_KEY} --api_id=${API_ID} --account_id=${ACCOUNT_ID}
python incap.py site security 35473495 --help
ls -l
cd export/
ls
ls -lrt
cat 55045384_www.api-np.anz_2019051
cat 55045384_www.api-np.anz_20190515-022737.json 
SITE_ID=$(cat site_creation.txt | awk -F: '{print $3}') && python incap.py site whitelist api.acl.whitelisted_ips $SITE_ID --ips=10.0.0.0/24,30.0.0.0/24 --api_key=${API_KEY} --api_id=${API_ID} 
cd ..
SITE_ID=$(cat site_creation.txt | awk -F: '{print $3}') && python incap.py site whitelist api.acl.whitelisted_ips $SITE_ID --ips=10.0.0.0/24,30.0.0.0/24 --api_key=${API_KEY} --api_id=${API_ID} 
SITE_ID=$(cat site_creation.txt | awk -F: '{print $3}') && python incap.py site whitelist api.acl.whitelisted_ips $SITE_ID --ips=10.0.0.0/24,30.0.0.0/24 --api_key=${API_KEY} --api_id=${API_ID} 
SITE_ID=$(cat site_creation.txt | awk -F: '{print $3}') && python incap.py site whitelist whitelisted_ips $SITE_ID --ips=10.0.0.0/24,30.0.0.0/24 --api_key=${API_KEY} --api_id=${API_ID} 
python incap.py --help
python incap.py site --help
python incap.py site acl --help
SITE_ID=$(cat site_creation.txt | awk -F: '{print $3}') && python incap.py site acl api.acl.whitelisted_ips $SITE_ID --ips=10.0.0.0/24,30.0.0.0/24 --api_key=${API_KEY} --api_id=${API_ID} 
SITE_ID=$(cat site_creation.txt | awk -F: '{print $3}') && python incap.py site whitelisted_ips $SITE_ID --ips=10.0.0.0/24,30.0.0.0/24 --api_key=${API_KEY} --api_id=${API_ID} 
SITE_ID=$(cat site_creation.txt | awk -F: '{print $3}') && python incap.py site acl whitelisted_ips $SITE_ID --ips=10.0.0.0/24,30.0.0.0/24 --api_key=${API_KEY} --api_id=${API_ID} 
SITE_ID=$(cat site_creation.txt | awk -F: '{print $3}') && python incap.py site acl blacklisted_ips $SITE_ID --ips=10.1.0.0/24,30.1.0.0/24 --api_key=${API_KEY} --api_id=${API_ID}
ls -lrt
python incap.py site upcert --help
SITE_ID=$(cat site_creation.txt | awk -F: '{print $3}') && python incap.py site upcert server.pem $SITE_ID --private_key=private_key.pem --api_key=${API_KEY} --api_id=${API_ID}
SITE_ID=$(cat site_creation.txt | awk -F: '{print $3}') && python incap.py site upcert  $SITE_ID --private_key=private_key.pem --api_key=${API_KEY} --api_id=${API_ID}
ls -lrt
ls -lrt
exit
ls -lrt
exit
ls -lrt
export ACCOUNT_ID="1284650"
export API_ID="32071"
export API_KEY="1b033a13-c10a-4d6b-a932-876007e55b9d"
ls -lrt
SITE_ID=$(cat site_creation.txt | awk -F: '{print $3}') && python incap.py site upcert  certifcate.pem $SITE_ID --private_key=private.pem --api_key=${API_KEY} --api_id=${API_ID}
ls -lrt
cat incap.py 
cat Sites/acl.py 
ls -lrt
ls -lrt
ls 
ls -lrt
cd Sites/
ls
ls -lrt
cat waf.py 
ls -l
cat site.py 
cd ..
ls -l
cd Accounts/
ls
ls -l
cd ..
curl
ls -l
cat site_creation.txt 
python incap.py site list
python incap.py site list
export ACCOUNT_ID="1284650"
export API_ID="32071"
export API_KEY="1b033a13-c10a-4d6b-a932-876007e55b9d"
python incap.py site list
ping google.com
exit
export ACCOUNT_ID="1284650"
export API_ID="32071"
export API_KEY="1b033a13-c10a-4d6b-a932-876007e55b9d"
python incap.py list
python incap.py site list
ping google.com
exit
