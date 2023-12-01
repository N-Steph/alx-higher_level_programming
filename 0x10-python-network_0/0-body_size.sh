#!/bin/bash
# Sends a request to a URL and displays the size of the body of the response
curl $1 -s --head | tail -n 2 | cut -d " " -f 2 | head -n 1 
