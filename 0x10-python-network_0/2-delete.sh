#!/bin/bash
# Display body of response message after sending a DELETE request
curl -sL --http1.1 -X DELETE --url "$1"
