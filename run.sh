#!/bin/bash
docker build --no-cache -t flasktesti .
docker run --name flasktest --expose=4000 -p 4000:5000 -d flasktesti:latest