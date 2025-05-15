#!/bin/bash

# Stop and remove the old container (if it's already running)
docker stop flask-container || true
docker rm flask-container || true

# Pull the latest Docker image from Docker Hub
docker pull abhirammanoj/flask-ecom:latest

# Run the updated container on port 80
docker run -d --name flask-container -p 80:80 abhirammanoj/flask-ecom:latest
