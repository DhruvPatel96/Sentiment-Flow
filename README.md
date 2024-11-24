# Distilbert Sentiment-Analysis
### Why distilbert model for Demo.?
- The choice of the (distilbert-base-uncased-finetuned-sst-2-english model) is based on its balance between performance and resource usage. DistilBert is a smaller, faster, cheaper, and lighter version of BERT. It retains 95% of BERT's performance while being 60% smaller and 60% faster. This makes it an excellent choice for deploying models in environments where resources are limited or where the model needs to be lightweight to reduce inference time. Personally, I wanted to use lightest possible model that I can test on my local system.

### Components :
### 1. Client (My case : Jupyter notebook)
The client sends HTTP requests to the Flask application. This could be a web browser making a request to a web page, or an API client sending a POST request to the /predict endpoint of the Flask application.
### 2. Flask Application
The Flask application acts as the web server. It listens for incoming HTTP requests on a specific port (my case : 5000). When a request is received, Flask routes the request to the appropriate handler function based on the URL and HTTP method. In this case, POST requests to /predict are handled by the predict function.
### 3. Gunicorn
Gunicorn is a WSGI HTTP server for Python web applications. It acts as an intermediary between the Flask application and the client. When a request is received by Flask, Gunicorn forwards the request to the Flask application. Gunicorn also manages the application's worker processes, which handle the actual processing of requests.
### 4. Docker Container
The Docker container encapsulates the Flask application, gunicorn, and the ML model. It provides an isolated environment where these components can run. The Docker container exposes a port (my case: 8000) to the host machine, allowing external clients to communicate with the Flask application.
### 5. Host Machine
The host machine runs the Docker container. When a client sends a request to the host machine on the exposed port (my case: 8000), the request is forwarded to the Docker container. Inside the container, gunicorn receives the request and forwards it to the Flask application. The Flask application processes the request, interacts with the ML model to make predictions, and sends a response back through gunicorn to the client.
### Communication Flow:
- The client sends an HTTP request to the host machine on port 8000.
- The Docker container receives the request and forwards it to gunicorn.
- Gunicorn forwards the request to the Flask application.
- The Flask application processes the request, interacts with the ML model, and sends a response back to gunicorn.
- Gunicorn forwards the response back to the Docker container.
- The Docker container sends the response back to the client.

This setup allows for efficient and scalable deployment of web applications that use machine learning models, leveraging the benefits of Docker for containerization and gunicorn for serving the application.

### NOTES:
- Major focus is on deployment (Contanarization) due to which model's performance and output format is kept minimal.
- Docker compose file have 2 variants in 1 file : 1) Build image from local (clone repo and build) OR 2) Pull image from [my docker hub repo](https://hub.docker.com/repository/docker/dhruv961211/lemay/general)
- Docker file have 2 variane in 1 file : 1) CPU based container OR 2) CUDA based container
- Comment and Uncomment required section 
