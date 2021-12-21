This is a Demo Test Suite aimed to demonstrate basic expertise in the field of AQA.
Author - Anna Lozynska


The application under test can be found here
https://github.com/microservices-demo/microservices-demo
https://microservices-demo.github.io/

Clone the application repository
git clone https://github.com/microservices-demo/microservices-demo
cd microservices-demo

Start the application via Docker Compose
docker-compose -f deploy/docker-compose/docker-compose.yml up -d

Open the Sock Shop web page
Using your browser, visit http://localhost/ to see the Sock Shop webpage.

Cleaning up
docker-compose -f deploy/docker-compose/docker-compose.yml down
