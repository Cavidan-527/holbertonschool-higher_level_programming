#!/bin/bash
# Displays the size of the HTTP response body in bytes
curl -s "$1" | wc -c
