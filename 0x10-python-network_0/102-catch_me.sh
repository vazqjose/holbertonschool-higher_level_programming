#!/bin/bash
# Script displays that causes the server to respond with a message
curl -s -L -d "You got me!" -X 'PUT' "0.0.0.0:5000/catch_me"
