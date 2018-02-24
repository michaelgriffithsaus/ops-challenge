#!/usr/bin/env bash
# Written by Michael Griffiths
# This script will pull the latest versions of the ops-challenge container and run it.

# Stop the script when an error occurs.
set -o errexit

# Puts the script in debug mode (will print every line to stdout before each line executes).
#set -o xtrace

# The local port to assign to the flask web server
# Change this port if you already have 8080 allocated to something else. 
PORT=8080 

# Pull the container from the Repo.
docker pull werfcoder/ops-challenge:latest

# Run the container.
docker run -d -p $PORT:8080 werfcoder/ops-challenge:latest 