#!/bin/bash
# Sends a POST request to the passed URL
curl -sL --http1.1 --url "$1" --data-raw email=test@gmail.com --data-raw subject="I will always be here for PLD"
 
