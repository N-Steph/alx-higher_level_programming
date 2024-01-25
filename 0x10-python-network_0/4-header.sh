#!/bin/bash
# Display body of a response message after sending a GET request with some data
curl -sL --http1.1 --url "$1" -G --data X-School-User-Id=98
