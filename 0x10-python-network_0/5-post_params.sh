#!/bin/bash
# sends a POST request to the passed URL and display the body of the response
curl $1 -s --data-raw email="test@gmail.com" --data-raw subject="I will always be here for PLD"
