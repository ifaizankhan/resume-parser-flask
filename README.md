## Machine Learning Project using Python Flask, BERT and Text Analysis and Processing

### Pre-requisites
Docker must be Installed in your system in order to execute it
Get it from here: https://docs.docker.com/get-docker/

### Execution
First of all pull the Docker image from Dockerhub

### docker pull ifaizankhan/mlworkingflask:latest
Second, Move to the directory where you have clone the GIT repository.

### cd /path to git repo/
Thirdly create the container from that Image, It contains all the dependencies for the script to execute

### docker run -itd -v $(pwd)://src -p 5000:5000 [image_id] bin/bash
Get inside the container that is being created using the container ID

### docker attach [container ID]
Finally you can find all the files of the repo inside the container, just go to

### cd /src
Inside the folder, run the project using

### python run.py
For Results on UI

https://localhost:5000/
