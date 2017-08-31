#!/bin/sh

gcc program.c -o program
cat program | base64 > program.txt
rm program
