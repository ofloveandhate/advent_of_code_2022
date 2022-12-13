#!/bin/bash


if [ -z $1 ];
	then
		# https://stackoverflow.com/questions/3601515/how-to-check-if-a-variable-is-set-in-bash
		echo "a first positional argument is required, the number of the challenge.  e.g. '1'";
		exit 1 # https://stackoverflow.com/questions/1378274/in-a-bash-script-how-can-i-exit-the-entire-script-if-a-certain-condition-occurs
fi


mkdir $1 && cp solution.py $1/ && touch $1/testinput.txt && touch $1/input.txt

