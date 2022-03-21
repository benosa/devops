## Works
We can run playbook with three tags:
    "nginx"     - install nginx on remote server without tls mode
    "ssl"       - create ssl certificate for nginx tls
    "mariadb"   - install mariadb on remote server
    "php-fpm"   - install php-fpm on remote server
    "wordpress"   - install wordpress on remote server

    If we need setup tls for nginx, we should run playbook with ssl flag before nginx flag run

    Run command 

    ansible-playbook ./main.yaml --tags="ssl,nginx,mariadb,php-fpm,wordpress"

-----------------------------------
## For SSL gen

## Before run - we need setup host in file hosts

Before starting you need:
1) install community crypto modules: 'ansible-galaxy collection install community.crypto'
2) install libselinux-python3: 'sudo yum install libselinux-python3'
3) install python3 module selinux: 'pip install selinux'
4) In file 'hosts' set 'ansible_host', 'ansible_port'
5) In file 'ssl-role/vars/main.yaml' set 'python_version', 'cert_host'
6) In file 'ssl-role/vars/main.yaml'  - set 'secret_ca_passphrase'
7) install community general modules: 'ansible-galaxy collection install community.general'

If we see Error: 
----
fatal: [localhost]: FAILED! => {"changed": false, "checksum": "9f69b05ca031ea121163d6888d0aab27fe91d046", "msg": "Aborting, target uses selinux but python bindings (libselinux-python) aren't installed!"}
---
need:

8) cp -r /usr/lib64/python3.6/site-packages/selinux $VIRTUAL_ENV/lib64/python3.6/site-packages
9) cp /usr/lib64/python3.6/site-packages/selinux/_selinux.so $VIRTUAL_ENV/lib/python3.6/site-packages

10) We can import CA.pem in browser (generated CA.pem is placed in "{{playbook_dir}}/etc/ca/ca-certificate.pem")

-----------------------------------
## For MariaDB

Run playbook:   **ansible-playbook ./main.yaml  --tags="mariadb**

Please edit **mariadb-role/vars/main.yaml** file and please set **user**, **password**, **dbname** variables