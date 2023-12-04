#!/bin/bash
# Sends a JSON POST request and displays body of the response
curl -X POST $1 -H "Content-Type: application/json" --data-urlencode @$2 -s
