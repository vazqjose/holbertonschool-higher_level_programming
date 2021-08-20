#!/bin/bash
# Script that takes in a URL, sends GET request, returns response body
curl -sb -H "Accept: application/json" $1
