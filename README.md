# bookstore
Create a simple bookstore for training 

# Step for config :
1. Install docker
     - optional: clean all containers and images for a fresh start:
     c.1: docker rm -vf $(docker ps -a -q)
     c.2: docker rmi -f $(docker images -a -q)

2. Run
    c.1: docker-compose up -d --build
    c.2: docker-compose up



# About :

Currently the application is composed of 3 services:
    1. Web Server: django
    2. In-memory-db: redis
    3. Async. task: celery

Recommendation: to connect postgresql bd as another service

From now on everyone will have to work this way.


Good luck!
Fave fun!