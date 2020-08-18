#!/bin/bash
# Sends a POST request to the URL with certain variables
curl $1 -s -X POST -d "email=hr%40holbertonschool%2Ecom&subject=I+will+always+be+here+for+PLD"
