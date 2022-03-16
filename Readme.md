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

#### Install kind

##### Install king cluster in your local machine 

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
##### Create the custer and the resurces

```
kind create cluster --config=config.yaml
kubectl apply -f deployment.yaml
kubectl create -f service.yaml 
```

#####	Expose nodePort and test the endpoint 

```
kubectl expose deployment hello-world --type=NodePort --name=example-service-hello-word
curl http://<public-node-ip>:<node-port> 
```
 
#### Automate the previous steps in a pipeline using  Jenkins 

4.	Jenkisfile Attached








