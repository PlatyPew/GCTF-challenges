# Cringeyroll
Changing HTML elements

<i>Creator - @Platy</i>

## Category
Sanity

## Question
>Here comes the anime awards! However, other mainstream anime are winning! As a fangirl of Yuri On Ice, I'm getting triggered. Hack the awards and make the points of Yuri On Ice 1000000! I'll give you the flag if you manage to.
>
>Connect via http://localhost:17454

### Hint
None.

## Setup Guide
Do `bash build.sh`

## Distribution
None.

## Solution
Most cringey challenge I have created ever.

<b>Inspect the elements</b>
```html
<form action="index.php" method="POST">
	<h3>Rate</h3>
	<select name="yoi">
		<option value="1">1</option>
		<option value="2">2</option>
		<option value="3">3</option>
		<option value="4">4</option>
		<option value="5">5</option>
		<input type="submit" value="Submit">
	</select>
</form>
```
Change the value from 1 to 1000200 and hit submit

Points will now be 1,000,000

<b>Curl</b>
```bash
curl 'http://192.168.159.131:30000/index.php'--data 'yoi=1000200' | grep GCTF
```

Too easy.

### Flag
`GCTF{7h3_4n1m3_4w4rd5_w3r3_r1663d}`

## Credits
Some challenge in hack this site.

## Recommended Reads
None.
