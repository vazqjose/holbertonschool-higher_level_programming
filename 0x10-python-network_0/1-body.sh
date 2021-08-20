#!/bin/bash
# Script that takes in a URL, sends GET request, returns response body
curl -s -o /dev/null -w "%{http_code}" $1
