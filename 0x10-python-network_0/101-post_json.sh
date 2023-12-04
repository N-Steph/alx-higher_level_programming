#!/bin/bash
# Sends a JSON POST request and displays body of the response
curl -X POST $1 -H "Content-Type: application/json" -d @$2 -s
