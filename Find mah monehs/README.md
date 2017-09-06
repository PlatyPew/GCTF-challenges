# Find mah monehs
Testing on programming knowledge

<i>Creator - @Platy</i>

## Category
Programming

## Question
>NEEDZ HALPZ ME 2 FIND MAH MONEHS 2 BUY SUM GAMEZ. ME WANTS $100. CAN HALP PLZ? THX M8!
>
>Connect via `nc localhost 13337` (Change the IP to server)

### Hint
PATH FINDIN ALGORITHM M8

## Setup Guide
Do `bash start.sh` and run `docker start money`

## Distribution
Zip file containing 5 sample files for testing
- monehs.zip
  - sample1.txt
  - sample2.txt
  - sample3.txt
  - sample4.txt
  - sample5.txt

## Solution
To start off, this challenge has nothing to do with lolcat I just wanted to have some fun.

Alright so getting right into it, when we connect to a service we are greeted with some instructions.

```
 -  -  -  -  -  -  -  -  -  - 
 -  -  -  -  -  -  -  -  -  - 
 $  +  -  -  -  -  -  -  -  - 
 -  +  +  +  -  +  +  +  -  - 
 -  +  +  -  +  +  +  +  -  - 
 -  +  +  +  +  @  +  +  +  - 
 +  +  +  +  +  +  +  -  -  - 
 +  +  +  +  +  +  -  -  -  - 
 +  +  -  -  +  -  -  -  -  - 
 +  +  -  -  -  -  -  -  -  -

TEH ANZWR WILL BE: aaaawwwa
```
Basically, we want to give directions to get from the `@` to the `$` using the 'wasd' keys to navigate. Easy enough right? The program only gives us 3 seconds to calculate the path. So it's time to program.

Using sockets in python, we can create a pathfinding algorithm.

Receive the input, format it nicely so that python can understand the data

Run the path finding algorithm. (I used flood fill but you are free to use A* or dijkstra)

Once you have completed, you can run your program and voila!

Working program in solution.

### Flag
`GCTF{1_w45_br0k3_bu7_n0_m0r3}`

## Credits
None.

## Recommended Reads
None.
