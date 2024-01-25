#!/bin/bash
# Display body of a response message after sending a GET request with some data
curl -sLG --http1.1 --url "$1" --data X-School-User-Id=98
