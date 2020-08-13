# bookstore - branch DGA
Create a simple bookstore for training 

# Steps for run 
1. Install docker

2. Optional: clean all containers and images for a fresh start:
    - c.1: docker rm -vf $(docker ps -a -q)
    - c.2: docker rmi -f $(docker images -a -q)

2. Run
     - c.1: docker-compose build 
     - c.2: docker-compose up


3. Stop 
     - c.1: CTRL+C (stop all up containers)
     - c.2: docker-compose down -v 

# About 

Currently the application is composed of 4 services:

1. Web Server: django
2. In-memory-db: redis
3. Async. task: celery
4. Database: postgresql

From now on everyone will have to work this way.


# Good luck!
# Fave fun!