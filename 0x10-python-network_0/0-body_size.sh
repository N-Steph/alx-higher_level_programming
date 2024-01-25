#!/bin/bash
# Display the size of the body of a response message after sending a request
curl GET "$1" HTTP/1.1 | grep Content-Length | cut -d " " -f 2
