#!/bin/bash
# Takes in a URL displays all HTTP methods the server will accept
curl $1 -s --request OPTIONS
