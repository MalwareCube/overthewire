#!/bin/bash

if [[ -z "$1" ]] || [[ -z "$2" ]]; then
	echo "Usage: ./natas.sh levelname password"
else
	curl http://$1.natas.labs.overthewire.org -u $1:$2
fi
