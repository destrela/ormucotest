# Cats or Dogs application

## Application
- The aplication was writen with flask and is inside the catsordogs folder
- All database connection configurations are made trough environment variables:
	- COD_USER
	- COD_PASSWORD
	- COD_DATABASE
	- COD_HOST
- The database has only one table with three columns:
  - name
	- color
	- pet

## Infrastructure
- The application is served by a uwsgi server
- Has a Nginx server that connect, via file socket, to the uwsgi server and provides the acces to internet
- The http server uses ssl to encrypt the data
- All http request are redirect to the https server
- The database server runs in other machine than http/application server

## Ansible playbook
- The playbook is divided in three plays:
	- One to instantiate the ec2 machines
	- Other to configure MySQL server
	- And other to configure the http/application server
- All variables that contain sensitive information, such AWS_SECRET_ACCESS_KEY, COD_PASSWD, etc. are in files protected by ansible vault
- The ansible vault password is **ormucopass**
- The file protected by ansible-vault are:
	- deploy/group_vars/all/aws_vars.yaml
	- deploy/group_vars/all/keys.yaml
	- deploy/group_vars/all/mysql.yaml
	- deploy/roles/nginx/files/catsordogs.key
- All ec2 instances were made using id_rsa_ormuco.pub in deploy/key_files folder
- The ssh private key goes separately and its final path must be configured in SSH_PRIVATE_KEY in group_vars/all/local_public_key.yaml
- The user centos must be used to connect the instances: ssh -i <private_key> -l centos <instance_address>

## Instances
- The ip addresses of the two instance already created are:
	- catsordogs: 54.160.155.55
	- mysql: 54.242.185.191


