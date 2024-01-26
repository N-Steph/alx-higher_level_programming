#!/bin/bash
# Display only the status codeof a request
curl -sL --http1.1 -w "%{http_code}" --url "$1" -o /dev/null
