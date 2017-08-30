#!/bin/bash

if [ "$1" = "1" ]
then
	rm -f ./*.pyc
	rm -f ./*.pyo
	python -O -m py_compile ./*.py
elif [ "$1" = "0" ]
then
	rm -f ./*.pyc
	rm -f ./*.pyo
fi
