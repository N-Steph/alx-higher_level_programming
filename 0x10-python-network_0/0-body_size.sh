#!/bin/bash
# Sends a request to a URL and displays the size of the body of the response
curl $1 -s --head | grep Content-Length | cut -d " " -f 2
