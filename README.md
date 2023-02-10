### Homework-1-Build-your-own-Dockerfile-Image-and-Container

Git-Repo for solution code  : https://github.com/jesalshah14/CloudComputing_Homework-1-Build-your-own-Dockerfile-Image-and-Container.git

#### API Urls for backend Microservices & services provided.
1. Service1  - Fetch weather based on city name<br/>

    To run in browser   : http://localhost:5000/zip/Chicago<br/>
    To run with curl    : curl http://127.0.0.1:5000/zip/Chicago<br/>

2. Service2  - Fetch weather based on zipcode<br/>

    To run in browser   : http://localhost:5001/weather/94560<br/>
    To run with         : curl http://127.0.0.1:5001/weather/94560<br/>
    
## Service1

#### Steps to create service & run 
1.created service1.py file with code<br/>
2.cmd to run the app locally  : python service1.py<br/>
3.To test it in broswer       : http://localhost:5000/zip/Chicago<br/>
4.To test it in curl          : curl http://127.0.0.1:5000/zip/Chicago<br/>

### Create new network for both the service to communicate with each other over network
1.cmd to create network  : docker network create mynet
                
#### Steps to dockerize the service
1.created docker file with code<br/>
2.cmd to build : docker build -t zip .<br/>
3.cmd to run   : docker run --network mynet -p 5000:5000 --name zip zip<br/>

## Service2

#### Steps to create service & run 
1.created service2.py file with code<br/>
2.cmd to run the app locally  : python service2.py<br/>
3.To test it in broswer       : http://localhost:5001/weather/94560<br/>
4.To test it in curl          : curl http://127.0.0.1:5001/weather/94560<br/>
                
#### Steps to dockerize the service & run 
1.created docker file with code<br/>
2.cmd to build : docker build -t weatherservice .<br/>
3.cmd to run   : docker run --network mynet -p 5001:5001 --name weatherservice weatherservice<br/>


cmd to check images: docker images<br/>
cmd to check containers running: docker ps<br/>
         
### For screenshots : please refer the screenshot_new word document.
