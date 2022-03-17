# Deployment of a rest api application in a Kubertates cluster

In this repository we will see how to deploy and automate a single rest api Flask application in Kubernetes kind with Jenkins.

## Tolls / Pre-requirements 📋

- Flask to create the application
- Docker to package the application
- Docker hub to stores the  Docker images.
- Kubectl to expose the application
- Jenkins to automate the deployment
- Git to store and version control of the code
- Kind Kubernetes cluster

## Starting  🚀

### Repo description
 
- app.py : Application Based in Flask which returns { "hello" : "world" } to a GET request at the endpoint /helloworld
- Dockerfile : File used to build the image
- requirements.txt : file used when the docker image is built to by to install Flask
- pipeline.jenkinsfile : file used by jenkins to automate the deploymnet

### Installing and testing Pre-requirements for the deployment with Jenkins

1) Clone the repo to the machine
  ```
  git clone https://github.com/ezequiellladoce/flask-tutorial.git
  ```

### Test the flask app

1) Install Python pip

  ```
  apt install python3-pip
  ```

2)  Install Flask

   ```
     pip install flask  
   ``` 

3) Test de App

    - In the same folder that you have the app run the command  

    ```
     python3 app.py
    ```
    - You will get on the terminal:

     ![Image text](https://github.com/ezequiellladoce/Deploy_App_in_Kubernetes/blob/master/Images/test_app.PNG)   

    - Put In your browser:

    ```
        http://localhost:105/hello/
    ```
  
    - You will get on the browser: 

      ![Image text](https://github.com/ezequiellladoce/Deploy_App_in_Kubernetes/blob/master/Images/firefox.PNG)

### Package the image

1) Install docker according https://docs.docker.com/engine/install/

2) To build the image:

  ```
  docker build -t flask-tutorial:latest .
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
docker tag rest-api <your_user>/deploy_1:V0.0.0.1
```
6) Log in docker hub

```
docker login 
```
```
Login with your Docker ID
Username : 
Password:
```

7) Pushing the image to docker registry
 
```
docker push <your_user>/deploy_1:V0.0.0.1
```
### Kubernetes kind deployment

#### Install king cluster on your local machine 

```
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.10.0/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin
```
2) Test  the installation

```
kind version
kind v0.10.0 go1.15.7 linux/amd64
```
#### Create the custer and the resurces

```
kind create cluster --config=config.yaml
kubectl apply -f deployment.yaml
kubectl create -f service.yaml 
```

####	Expose nodePort and test the endpoint 

```
kubectl expose deployment hello-world --type=NodePort --name=example-service-hello-word
curl http://<public-node-ip>:<node-port> 
```
 
## Automate the previous steps in a pipeline using  Jenkins  📦

### Install Jenkins

1) Install Jenkins Server according  https://www.jenkins.io/doc/book/installing/linux/ in the same machine that you have installed all the Pre-requirements

### Create the Pipeline 

1) Create a new pipeline script and Configure the following parameters

insertar imagen

- Definition ----> Pipeline Script from GitSCM
- SCM ----> Git
- Repository URL ----> https://github.com/ezequiellladoce/flask-tutorial.git
- Branch Specifier ----> */master
- Script Path ----> pipeline.jenkinsfile

3) Build the Job







