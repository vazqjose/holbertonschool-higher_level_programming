#!/bin/bash
# Script that takes in a URL, sends GET request, returns response body
if (( $(curl -s -o /dev/null -w "%{http_code}" $1) == 200)) ; then curl -s $1 ; fi
