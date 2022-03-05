##Before run - we need setup host in file hosts

##Commands for CREATE/REMOVE users

Create users:   ansible-playbook ./create_users.yaml  --vault-password-file key.txt

Remove users:   ansible-playbook ./remove_users.yaml  --vault-password-file key.txt


key.txt file is included key for decrypt users.yaml file
users.yaml file is included encrypted data of five users