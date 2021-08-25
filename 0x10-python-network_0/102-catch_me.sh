#!/bin/bash
# Script displays that causes the server to respond with a message
curl -s -L --local-port 5000 "0.0.0.0:5000/catch_me" "$1"
