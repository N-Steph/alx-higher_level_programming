#!/bin/bash
# sends a GET request to a URL and displays the body of the reponse
curl $1 -s --header "X-School-User-Id: 98"
