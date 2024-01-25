#!/bin/bash
# Display body of a response message after sending a GET request with some data
curl -sL --http1.1 -H "X-School-User-Id: 98" --url "$1"
