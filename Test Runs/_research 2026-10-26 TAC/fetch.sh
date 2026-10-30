#!/bin/sh
# usage: fetch.sh URL OUTFILE  (SEC EDGAR with the operator's User-Agent)
curl -s -H "User-Agent: Chris Hrehor chrehor36@gmail.com" "$1" -o "$2"; sleep 0.3
