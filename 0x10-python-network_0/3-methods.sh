#!/bin/bash
# Display all HTTP methods the server will accept for a particular url
curl -sLI --http1.1 --url "$1" | grep "Allow" | cut -d ":" -f 2 | sed 's/^[ \t]*//'
