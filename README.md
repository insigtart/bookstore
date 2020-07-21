# How to create a new branch
1. git branch "name_of_branch" (from your Django env)

- comenzi aditionale: git branch --list
					  git status
					  git branch
2. git checkout "name_of_branch" (to switch from the master branch to yours)
3. git add .
4. git commit -m "Add my branch"
5. git push --- git push --set-upstream origin "name_of_branch"


# bookstore
Create a simple bookstore for training 

# Steps for run 
1. Install docker

2. Optional: clean all containers and images for a fresh start:
    - c.1: docker rm -vf $(docker ps -a -q)
    - c.2: docker rmi -f $(docker images -a -q)

2. Run
     - c.1: docker-compose build 
     - c.2: docker-compose up



# About 

Currently the application is composed of 3 services:

1. Web Server: django
2. In-memory-db: redis
3. Async. task: celery
4. Recommendation: to connect postgresql bd as another service

From now on everyone will have to work this way.


