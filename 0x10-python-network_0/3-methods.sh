#!/bin/bash
# Display the body of the response after sending a DELETE request
curl -sL --http1.1 -X DELETE --url "$1"
