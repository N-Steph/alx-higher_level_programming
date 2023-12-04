#!/bin/bash
# Displays only the status code of an HTTP response
curl -o /dev/null -X GET $1 -s -w %{http_code}
