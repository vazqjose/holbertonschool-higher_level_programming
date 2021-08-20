#!/bin/bash
# Script that takes in a URL, returns size of body
curl -s $1 --include | grep -i Content-Length | awk '{print $2}'
