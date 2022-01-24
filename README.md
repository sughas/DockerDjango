###Sample Django project in a docker-compose

#Steps to run the Project in local machine

#Install docker 

https://docs.docker.com/engine/


#Install docker-compse

https://docs.docker.com/compose/install/

docker-compose run django django-admin startproject core .

#To Check running of docker files

docker ps -a

#To bring up continer 
docker-compose up

#To bring down continer 
docker-compose down

#To check responce use this URL

http://0.0.0.0:8000/HelloWorld/

DB connection and other will be added in future commit's


