#!/bin/bash
# Takes in a URL displays all HTTP methods the server will accept
curl $1 -s -i -X OPTIONS | grep Allow | cut -d " " -f 2- | tr -d "\n" 
