#!/bin/bash
# Display body of a response message after sending a GET request with some data
curl -sL --http1.1 --data X-School-User-Id=98 --url "$1"
