Before starting you need:
1) install community crypto modules: 'ansible-galaxy collection install community.crypto'
2) In file 'hosts' set 'ansible_host', 'ansible_port'
3) In file 'main.yaml' set 'python_version', 'cert_host'
4) In file 'main.yaml' line 6 - set 'secret_ca_passphrase'
5) In file 'main.yaml' line 6 - set 'secret_ca_passphrase'

If we see Error: 
----
fatal: [localhost]: FAILED! => {"changed": false, "checksum": "9f69b05ca031ea121163d6888d0aab27fe91d046", "msg": "Aborting, target uses selinux but python bindings (libselinux-python) aren't installed!"}
---
need:

6) cp -r /usr/lib64/python3.6/site-packages/selinux $VIRTUAL_ENV/lib64/python3.6/site-packages
7) cp /usr/lib64/python3.6/site-packages/selinux/_selinux.so $VIRTUAL_ENV/lib/python3.6/site-packages

8) We can import CA.pem in browser