## Window Install

## Download docker image;
```
docker pull docker/getting-started:latest
```

### Docker getting started
-d: run the container in detached mode (in the background)
-p: assigning and mapping port from the local host, 
-p 80:80 - map port 80 of the host to port 80 in the container
Container Port: Port 80
Host post: Host 80
docker images: To see the image list

Image name: 
```
docker/gettig started
docker run -d -p 80:80 docker/getting-started
```
### To verify if docker image is running
```
docker ps
```
### access on browser
```
localhost:80
```
### To stop docker container
```
docker ps - To get docekr contianer id
docker stop <docker ID>
```
###To remove docekr image 
```
docker image - to get docker image ID
docker image rm <Image ID>
docker image rm -f <Image ID>
```

# Running a flask app
```
python app.py
```
```
localhost:5000
```
### Creating Doker image
```
docker build -t docker_guide .
```
#### Executing docker file
```
docker run -p 5000:5000 docker_guide
```
#### Pusk Docker image to Docker hub
```
docker login
docker build -t <username>/docker_guide . 
docker push <username>/docker_guide:latest
```