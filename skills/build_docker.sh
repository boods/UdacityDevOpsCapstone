#!/usr/bin/env bash

# Build image and add a descriptive tag
docker build -t capstone-skills .

# Create dockerpath
dockerpath=youngphillip/capstone-skills

# Authenticate & tag
echo "Docker ID and Image: $dockerpath"
docker tag capstone-skills:latest $dockerpath:latest

# Push image to a docker repository
docker push youngphillip/capstone-skills:latest
