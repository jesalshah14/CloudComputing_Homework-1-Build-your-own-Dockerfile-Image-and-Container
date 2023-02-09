### Homework-1-Build-your-own-Dockerfile-Image-and-Container

Git-Repo for solution code  : https://github.com/jesalshah14/CloudComputing_Homework-1-Build-your-own-Dockerfile-Image-and-Container.git

#### API Urls for backend Microservices & services provided.
1. Service1  - Fetch zipcode based on city name<br/>

    To run in browser   : http://localhost:5000/zipcode?city=Chicago<br/>
    To run with curl    : curl http://127.0.0.1:5000<br/>

2. Service2  - Fetch weather based on zipcode<br/>

    To run in browser   : http://localhost:5001/weather?zip=94530<br/>
    To run with         : curl http://127.0.0.1:5001/weather?zip=94550<br/>
    
## Service1

#### Steps to create service & run 
1.created service1.py file with code<br/>
2.cmd to run the app locally  : python service1.py<br/>
3.To test it in broswer       : http://localhost:5000/zipcode?city=Chicago<br/>
4.To test it in curl          : curl http://127.0.0.1:5000/zipcode?city=Chicago<br/>
                
#### Steps to dockerize the service
1.created docker file with code<br/>
2.cmd to build : docker build -t zipcodeservice .<br/>
3.cmd to run   : docker run -p 5000:5000 zipcodeservice<br/>
4.cmd to check images: docker images<br/>
5.cmd to check containers running: docker ps<br/>

## Service2

#### Steps to create service & run 
1.created service2.py file with code<br/>
2.cmd to run the app locally  : python service2.py<br/>
3.To test it in broswer       : http://localhost:5000/weather?zip=94530<br/>
4.To test it in curl          : curl http://127.0.0.1:5000/weather?zip=94530<br/>
                
#### Steps to dockerize the service & run 
1.created docker file with code<br/>
2.cmd to build : docker build -t zipcodeservice .<br/>
3.cmd to run   : docker run -p 5000:5000 zipcodeservice<br/>
4.cmd to check images: docker images<br/>
5.cmd to check containers running: docker ps<br/>
         
## For screenshots : please refer the word document.
