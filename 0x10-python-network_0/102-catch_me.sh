#!/bin/bash
# Sending a request that causes server to respond with message "You got me!"
curl -sLX PUT -F user_id=98 -H "Content-Type: multipart/form-data" "$1"
