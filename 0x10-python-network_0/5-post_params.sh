#!/bin/bash
# sends a POST request to the passed URL and display the body of the response
cur $1 --data-row email="test@gmail.com"&subject="I will always be here for PLD" --dump-header stdout -s
