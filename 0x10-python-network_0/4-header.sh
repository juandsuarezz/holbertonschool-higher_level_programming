#!/bin/bash
# Sends a GET request and displays the body of the response with custom header
curl $1 -s -X GET -H "X-HolbertonSchool-User-Id: 98"
