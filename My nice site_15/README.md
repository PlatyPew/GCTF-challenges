# My nice site
Curl doesn't run Javascript

<i>Creator - @Platy</i>

## Category
Web 10

## Question
>Void has been working hard during the holidays. He says he has a very nice website that he coded. However, I cannot seem to open it. Can you help me?

`http://<ip address>:17566`

### Hint
None.

## Setup Guide
Do `bash build.sh`

## Distribution
None.

## Solution
There is Javascript running a script that will crash the browser. Since curl doesn't load Javascript, we can use that

Do `curl <ip address>:17566` to get the flag

### Flag
`GCTF{j4v45cr1p7_15_d4n63r0u5}`

## Credits
Yong Ze for coming up with the idea

## Recommended Reads
None.