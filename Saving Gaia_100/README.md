# Saving Gaia
Testing on Local File Inclusion exploit, hash length extension attacks and finding environment variable.

<i>Creator - @Platy</i>

## Category
Web 100

## Question
>Please save the environment to get the flag!
>
>Connect via `http://<ip address>:17565`

### Hint
`The journal contains the necessary information to find the PHP source code`

`What happens to nano when it receives a SIGHUP or SIGTERM when it is running?`

## Setup Guide
Do `sudo bash build.sh`

## Distribution
No files to be distributed

## Solution
A pretty simple challenge if you know what a `hash length extension` attack is.

Upon opening up the website, we are told to save the environment. Clicking on one of the links just links to a video on YouTube. Nothing there. Upon opening up the page source, we are greeted with this:
```html
<form action="view.php" method="POST">
	<input type="hidden" name="magic" value="6895875">
	<input type="hidden" name="file" value="66696c656c6f636174696f6e2c6c6973742e747874">
	<input type="hidden" name="mac" value="48b49f65a86cd617e5c7423d23a67738c4057d06">
	<p>Just look at how many people have pledged to save the environment!</p>
	<input class="btn btn-success btn-lg" type="Submit" value="Show">
</form>
```

There is a form which is submitting 3 values. One for the file location, one of the mac and one for a value "magic" value. Clicking one the link <i>'Click here to save the environment'</i> we are redirected to `notsoeasy.html` and viewing the page source, we are shown this:
```html
<section id="section3" class="container-fluid">
	<!-- It is said that one day, robots will help save the environment -->
	<h3>Saving the environment ain't that easy</h3>
	<p><a href="index.html">Go back</a></p>
</section>
```
<i>'It is said that one day, robots will help save the environment'</i>. You can assume that it is referring to `robots.txt`. Upon opening that, we get something very interesting!

```
User-agent: *
Disallow: /my_journal.txt
```

Now we can head over to `my_journal.txt` and see what's inside

```
10/9/2017:	Learning how to code php! I have some HTML knowledge after my WCD teacher's constant preaching about going to w3schools.

11/9/2017:	Alright! My senior said that vim is far superior to nano. Time to test that out!

12/9/2017:	Going back to nano editor. I'm too dumb for vi, but I won't tell my senior that.

13/9/2017:	Nano is best editor obviously... I can code in php and it has nice colours!

15/9/2017:	My laptop battery spoilt and those stingy companies only gave 1 year warranty on that. Someone accidentally tripped over my wire and my screen blacked out. Thanks a lot!

22/9/2017:	Finished the first php prototype of my program!

23/9/2017:	Just need to figure out how to read files and maybe a password... Who knows?

25/9/2017:	I have a working page now. Amazing! I should tell all my friends about it. Hopefully, they will save the environment too!
```

In the journal, we are shown that the developer's computer was shutdown unexpectedly. Nano has a useful feature which appends the suffix `.save` when nano is closed unexpectedly.

So going to `view.php.save`, we are shown an older version of the source code of `view.php`.

```php
<?php
	$SECRET = ""; // To do in the future
	$file = $_POST["file"];
	$mac = $_POST["mac"];
	$magic = $_POST["magic"];
	for( $i = 0; $i <= strlen($file); $i++ ) {
		$num1 += ord($file[$i]);
	}
	for( $i = 0; $i <= strlen($mac); $i++ ) {
		$num2 += ord($mac[$i]);
	}
	$num3 = $num1 * $num2 - $num1 - $num2;
	if ($num3 == $magic) {
		$file = pack("H*",$file);
		$hash = hash("sha1",$SECRET.$file);
		$file = explode(",",$file);
		$file = $file[sizeof($file)-1];
		if ($hash === $mac) {
			// Figure out how to read from files
		} else {
			echo "You are not authorised to view this file!";
		}
	} else {
		echo "You are not authorised to view this file!";
	}
?>
```

This shows the algorithm used to open the file. Let's see if we can conduct a Local File Inclusion exploit! All we need now is a way to change the inputs to read from the file we want.

Upon decoding the file from hex, we are given this: `filelocation,list.txt`. All we need to do now is to change the data so that it will point to `/proc/self/environ` which is where the flag is stored.

But how can we change the input? There is a message authentication code that prevents us from just entering any files. Introducing the hash length extension attack.

Hash length extension works because the mac was generated with terrible algorithm such as this one. `hash(<secret key> + <message>) = mac`

Caluculate the formula `$num3 = $num1 * $num2 - $num1 - $num2;` to get `magic`

Since we don't know the length of `$SECRET`, we can brute force the values.

Working exploit in `solution/saltgen.py`

### Flag
`GCTF{6l0b4l_w4rm1n6_15_r34lz}`

## Credits
Google CTF - 2017

Misc.

Mindreader - 50pts

Hashpump

## Recommended Reads
None.
