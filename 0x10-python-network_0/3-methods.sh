#!/bin/bash
# Takes in a URL displays all HTTP methods the server will accept
curl -X OPTIONS $1 -s -i | grep Allow | cut -d ":" -f 2 | sed 's/^[ \t]*//'
