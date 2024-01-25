#!/bin/bash
# Display all HTTP methods the server will accept for a particular url
curl -sL --http1.1 -X OPTIONS --url "$1"
