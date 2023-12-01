#!/bin/bash
docker build -t flaskttesti .
docker run --name flaskttest --expose=4000 -p 4000:5000 -d flaskttesti:latest