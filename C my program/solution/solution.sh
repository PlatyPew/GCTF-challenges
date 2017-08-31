#!/bin/sh

echo 'Converting to ELF binary...'
cat program.txt | base64 -d > program
chmod +x program
echo 'Brute forcing in progress...'
for i in {0..10000}
do
	echo $i | ./program | grep {
done
