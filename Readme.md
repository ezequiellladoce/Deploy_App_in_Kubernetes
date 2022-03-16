# Deployment of a rest api aplication in a Kubertates cluster

In this repository we will see how to deploy and  automate a single rest api aplication in Kubernetes. 

## Tolls / Pre-requirements 📋

- Flask to create the aplication
- Docker to package the aplication
- Docker hub to stores the  Docker images.
- Kubectl to expose the aplication
- Jenkins to automathe the deployment
- Git to store and version control of the code
- Kubernetes cluster

## Starting  🚀

### Repo description
 
- app.py : Application Based in Flask which returns { "hello" : "world" } to a GET request at the endpoint /helloworld
- Dockerfile : File used to buil the image
- requirements.txt : file used whn the docker image is built to by to install Flask
- pipeline.jenkinsfile : file used by jenkind to automate the deploymnet

### Deployment steps

#### Test the rest api app

1) Clone the repo to the machine
```
git glone ....

```
2) Install Python pip

```
apt install python3-pip

```

3)  Install Flask

   ```
     pip install flask  
   ``` 

4) Test de App

    - In the same folder that you have the app run the commnand 

    ```
     python3 app.py
    ```
    - You will get on terminal:

     ![Image text](https://github.com/ezequiellladoce/Deploy_App_in_Kubernetes/blob/master/Images/test_app.PNG)   

    - Put In your browser:

    ```
        http://localhost:105/hello/

    ```
  
    - You will get on the browser: 

      ![Image text](https://github.com/ezequiellladoce/Deploy_App_in_Kubernetes/blob/master/Images/firefox.PNG)

#### Packege the image

1) To build the image:

  ```
  docker build -t flask-tutorial:latest .
  ```

  ```
  docker run -d -p 5000:5000 --name=flask-hello flask-tutorial
  ```

2) To test Open browser and put

  ```
  http://localhost:5000/helloworld
  ```

3) In the browser you will get

    ![Image text](https://github.com/ezequiellladoce/Deploy_App_in_Kubernetes/blob/master/Images/test_docker.PNG)

4) Tag the Image

```
docker tag flask-tutorial deploy_1/v1.0

```
5) Push the Image

Retag the Docker image  as per the docker hub repository name

```
docker tag rest-api ezequielllado/deploy_1:V0.0.0.1
```
Log in docker hub

```
docker login 

Login with your Docker ID
Username : 
Password:

```

Pushing the image to docker registry
 
```

docker push <your user>/deploy_1:V0.0.0.1

```

#### Install kind

```
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.10.0/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin

```
Test  the installation

```
kind version
kind v0.10.0 go1.15.7 linux/amd64
```
Install king cluster in your local machine 

```
kind create cluster --config=config.yaml

```
Create the resurces

```
kubectl apply -f deployment.yaml
kubectl create -f service.yaml 
```

c.	Expose nodePort
i.	kubectl expose deployment hello-world --type=NodePort --name=example-service-hello-word
4-	Test that the endpoint of the deployed application works.
i.	curl http://<public-node-ip>:<node-port> 





































```



2-	Package the application in a Docker container using a Dockerfile
a.	Dockerfile attached
b.	requirements.txt attached
c.	Package
i.	docker build -t flask-tutorial:latest .
ii.	docker run -d -p 5000:5000 --name=flask-hello flask-tutorial
d.	Test
i.	Open browser http://localhost:5000/helloworld
3-	Deploy the application to a kubernetes cluster (for instance, using a local kubernets cluster such as "kind") and expose the application with a service (nodePort or loadBalancer)
a.	Deployment deployment.yaml
b.	Deploy
i.	kubectl apply deployment.yaml
c.	Expose nodePort
i.	kubectl expose deployment hello-world --type=NodePort --name=example-service-hello-word
4-	Test that the endpoint of the deployed application works.
i.	curl http://<public-node-ip>:<node-port> 

5-	Automate the previous steps in a pipeline using any CI service (Jenkins, Github Actions, Travis CI, GitLab pipelines...).
i.	CI/CD Jenkins
1.	Add the mentioned files to Git hub 
2.	The Kubernetes Kin runs in the same machine than Jenkins
3.	The machine has Kubeclt and docker installed 
4.	Jenkisfile Attached

6-	Write down your technical decisions, why you decided to use any of the languages/tools/frameworks
•	I have decided use:
o	Flask,  because is a microframework based in phyton easy to implement
o	Kubectl is the tool that is native for Kubernetes
o	Jenkins,  because is the CI/CD  more intuitive











En este repositorio veremos  como desplegar automatizar y securizar el despliegue de una infraestructura core (VPC - Security Groups - Internet Gateway - Subnet - Route Table) mediante  módulos Terrafom y crearemos en su interior un Servidor Jenkins. Este será creado con los parámetros almacenados en terraform S3 backend y configurado mediante Ansible.

Este despliegue está alineado con las buenas prácticas de seguridad.

- En la infraestuctura core crearemos:

  - La infraestructura con modulos de terrafom (VPC - Security Groups - Internet Gateway - Subnet - Route Table).
  - Las key_pairs para acceder a las instancias que creemos y su almacenamiento mediante el servicio AWS Secret Manager.
  - Creación de Backed S3 donde almacenaremos los parámetros de la  Infraestructura  

- En La creación desde terraform una instancia servidor Jenkins realizaremos:

  - La Creación de  una instancia  dentro la infraestructura core ya creada con los parámetros almacenados en el Backend.
  - Utilizaremos la función data de Terrafom para obtener la última imagen de ubuntu disponible en nuestra región de AWS.
  - Almacenaremos la ip publica en un S3 backend la instancia para luego utilizarla con Ansible.

- En la configuración del servidor de Jenkins mediante Ansible realizaremos:

 - Obtendremos la ip púbica de nuestra instancia desde el s3 backend
 - Configuraremos esta ip en el archivo hosts de Ansible
 - Con Ansible instalaremos en nuestra instancia:
    - Paquetes básicos
    - Jenkins
    - Docker


## Pre-requisitos 📋

- TERRAFORM .12 o superior
- AWS CLI
- CUENTA FREE TIER AWS
- Ansible

## Comenzando 🚀

### Descripción del repositorio:

En la carpeta 01_Deploy_Basic_infra tendremos el código para crear la infraestructura base, esta permitirá:

 - Crear la Infraestructura básica aws con modulos (VPC - Security Groups - Internet Gateway - Subnet - Route Table)
 - Crear desde terraform la clave mediante el recurso TLS Private Key
 - Almacenar la clave  creada en Aws Secrets Manager
 - Crear los outputs de los parámetros Subnet ID y Security Group ID
 - Guardar con la función Backend en S3 la información de la infraestructura creada.

 En la carpeta 02_EC2_Jenkins tendremos el código para crear la instancia EC2, este permitirá:

 - Crear la Instancia EC2 con la información almacenada en el Backed de S3.
 - Utilizar el recurso data terraform_remote_state para otener la ultima AMI ubuntu disponible en la región de Aws
 - Crear el output Public Ip y lo almacenamos en el Backend de la instancia.

 En la carpeta data 03_Configure_Basic_infra tendremos el código Ansible para Configurar el Jenkins Server:

 - En la carpeta Output_ip tendremos el código terraform para obtener la ip pública de la instancia creada para el Jenkins Server
 - En la Carpeta Ansible tendremos el playbook y el rol y las tareas para configurar el servidor.

### Descripción del Código (partes principales):

#### Infraestructura Core (carpeta 01_Deploy_Basic_infra)

##### Terrafom Backend

En el Main creamos el terraform Backend podremos almacenar la configuración de la infraestructura core creada y almacenarla en forma remota en un bucket S3.

```
terraform {
  backend "s3" {
    bucket = "backendbucket20210519"
    key    = "data_front/"
    region = "us-east-2"
  }
}
```

##### AWS Secret Manager

Con el recurso aws_secretsmanager_secret en el modulo ssh_keys creamos el Secrets en el servicio de AWS Secret Manager. El código es el siguiente:

```
resource "aws_secretsmanager_secret" "ec2-secret-key-c" {
  name = var.Secret_Key
  description = "Name of the secret key"
  tags = {
    Name = "EC2-Secret-Key"
  }
}
```

Con el recurso aws_secretsmanager_secret_version en el modulo ssh_keys cargamos la clave creada por el recurso tls_private_key. El código es el siguiente:

```
resource "aws_secretsmanager_secret_version" "secret_priv" {
  secret_id     = aws_secretsmanager_secret.ec2-secret-key-c.id
  secret_string = tls_private_key.priv_key.private_key_pem
}

```

#### Deploy Ec2 Jenkins Server  

##### Terraform remote state (carpeta 02_EC2_Jenkins)

El data Terraform remote state nos permite extraer los outputs grabados  del  remote backend.

```

data "terraform_remote_state" "if_trs" {
  backend = "s3"
  config = {
      bucket = "backendbucket20210519"
      key    = "data_front/"
      region = "us-east-2"
  }
}
```
El recurso data nos permite extraer el Ami de la última imagen de ubuntu de nuestra región

```
data "aws_ami" "lubuntu" {
 most_recent     = true
 owners = ["099720109477"]

 filter {
   name   = "name"
   values = ["ubuntu/images/hvm-ssd/ubuntu-*-*-amd64-server-*"]
 }
 filter {
   name   = "virtualization-type"
   values = ["hvm"]
 }
}
```

Con la información de los outputs del data Terraform remote tendremos la subnet id , el vpc security group ids y el key name para utilizarlos en la creación de la instancia.

```

resource "aws_instance" "ec2" {
   ami           = data.aws_ami.lubuntu.id
   instance_type = var.inst_type
   associate_public_ip_address = true
   subnet_id                   = data.terraform_remote_state.if_trs.outputs.snt_id
   vpc_security_group_ids      = [data.terraform_remote_state.if_trs.outputs.sgs_id]
   key_name                    = data.terraform_remote_state.if_trs.outputs.k_name
   tags = {
         Name = "EC2_Jenkins_Instance"
   }
}
```

Creams el backend para almacenar los datos de la instancia

```
terraform {
  backend "s3" {
    bucket = "backendbucket20210519"
    key    = "data_front_2/"
    region = "us-east-2"
  }
}

```

## Despliegue 📦

### Preparamos el ambiente:

1) Instalamos Terrafom https://learn.hashicorp.com/tutorials/terraform/install-cli
2) Creamos cuenta free tier en AWS  https://aws.amazon.com/
3) Instalamos AWS CLI https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html
4) Creamos usuario AWS en la sección IAM con acceso Programático y permisos de administrador https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html   
5) Configuramos el AWS CLI https://docs.aws.amazon.com/polly/latest/dg/setup-aws-cli.html
6) Creamos en un Buket S3 las carpetas data_front_1 y data_front_2.
7) Instalamos Ansible https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html

### Ejecutamos el despliegue

#### Despliegue de Infraestructura Core.

1) Clonamos el repositorio
2) Ingresamos en la carpeta 01_Deploy_Basic_infra
3) Editamos el archivo main.tf y cambiamos el bucket en el terraform backend.
4) Ejecutamos terraform int, para que terraform baje los plugins necesarios
5) Ejecutamos terraform plan
6) Ejecutamos terrafom apply para que realice el despliegue.
7) Verificamos que realice los outputs.
8) Vamos a muestra cuenta de AWS para verificar que se haya realizado el despliegue

#### Despliege de la Instancia.

1) Ingresamos en la carpeta 02_EC2_Jenkins
2) Editamos el archivo Deploy-EC2.tf y cambiamos el bucket en el terraform backend y en el data terraform remote state
3) Ejecutamos terraform int, para que terraform baje los plugins necesarios
4) Ejecutamos terraform plan
5) Ejecutamos terrafom apply para que realice el despliegue.
6) Verificamos que realice el output.
7) Vamos a muestra cuenta de AWS para verificar que se haya realizado el despliegue

#### Configuramos la instancia

1) Ingresamos en la carpeta 03_Configure_Basic_infra/Output_ip
2) Editamos el archivo Public_ip_from_backend.tf y cambiamos el bucket en el data terraform remote state
3) Ejecutamos terraform int, para que terraform baje los plugins necesarios
4) Ejecutamos terraform plan
5) Ejecutamos terrafom apply para que realice el despliegue.
6) Verificamos que realice el output.
7) Ejecutamos

```
echo "[jenkins_server]" > /etc/ansible/hosts
```
Para configurar el achivo hosts

```
terraform output public_ip >> /etc/ansible/hosts
```
Para incluir la ip de la instancia en el archivo hosts

En la carpeta 03_Configure_Basic_infra/Ansible, Con el Aws cli extraemos la clave del Secret Manager

```
aws secretsmanager get-secret-value --secret-id "ec2-key-c" --region "us-east-2" --query 'SecretString' --output text > key.pem

```
Le asignamos permisos

```
chmod 400 key.pem
```
Ejectamos el playbook

```
 ansible-playbook Ansible/playbook.yml -u ubuntu --key-file key.pem
```
