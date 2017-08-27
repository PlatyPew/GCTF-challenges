# Saving Gaia
Testing on Local File Inclusion exploit, hash length extension attacks and finding environment variable.

<i>Creator - @Platy</i>

## Category
Web

## Question
Please save the environment to get the flag!

## Hint
`Are you feeling salty? Would you like to have a hashbrown?`

## Setup
Do `bash start.sh`

## Solution
A pretty simple challenge if you know what a `hash length extension` attack is.

Upon opening up the website, we are told to save the environment. Clicking on one of the links just links to a video on YouTube. Nothing there. Upon opening up the page source, we are greeted with this:
```html
<html>
	<head>
		<title>Saving Gaia</title>
	</head>
	<body>
		<h1>Please save the environment!</h1>
		<form action="view.php" method="POST">
			<!-- Read from file location -->
			<input type="hidden" name="file" value="66696c656c6f636174696f6e2c6c6973742e747874">
			<input type="hidden" name="mac" value="5dcd3edd3680496a165bfd2a1b3fec397cde0a12">
			Just look at how many people have pledged to save the environment! <input type="Submit" value="Show">
		</form>
		<p>Don't feel like saving the world? Watch
			<a href="https://www.youtube.com/watch?v=s4pIQ238PFc">this</a>!
		</p>
		<a href="notsoeasy.html">Click here to save the environment</a>
	</body>
</html>
```

There is a form which is submitting 2 values. One for the file location and one of the mac. Clicking one the link <i>'Click here to save the environment'</i> we are redirected to `notsoeasy.html` and viewing the page source, we are shown this:
```html
<html>
	<head>
		<title>Saving Gaia</title>
	</head>
	<body>
		<!-- It is said that one day, robots will help save the environment -->
		<h3>Saving the environment ain't that easy</h3>
		<a href="index.html">Go back</a>
	</body>
</html>
```
<i>'It is said that one day, robots will help save the environment'</i>. You can assume that it is referring to `robots.txt`. Upon opening that, we get something very interesting!
```php
<?php
	$SECRET = 20 chars long
	$file = $_POST["file"];
	$mac = $_POST["mac"];
	$hash = hash("sha1",$SECRET.$file);
	$file = pack("H*",$file);
	$file = explode(",",$file);
	$file = $file[sizeof($file)-1];
	if ($hash === $mac) {
		// Read file
	} else {
		echo "You are not authorised to view this file!";
	}
?>
```
This shows the algorithm used to open the file. Let's see if we can conduct a Local File Inclusion exploit! All we need now is a way to change the inputs to read from the file we want.

Upon decoding the file from hex, we are given this: `filelocation,list.txt`. All we need to do now is to change the data so that it will point to `/proc/self/environ` which is where the flag is stored.

But how can we change the input? There is a message authentication code that prevents us from just entering any files. Introducing the hash length extension attack.

Hash length extension works because the mac was generated with terrible algorithm such as this one. `hash(<secret key> + <message>) = mac`

Using hashpump, we are able to append our own file location and the new generated hash. For the file, we are using `66696c656c6f636174696f6e2c6c6973742e74787480000000000000000000000000000000000000000001482c2f70726f632f73656c662f656e7669726f6e` and for the mac we are using this `641c68dcb0b1adc7f2d100717b5cc796b11287a6`. Press show and this pops up:
```
['LANGUAGE=en_SG:en\x00APACHE_RUN_DIR=/var/run/apache2\x00APACHE_PID_FILE=/var/run/apache2/apache2.pid\x00Flag=flag{this_is_a_flag}\x00PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\x00APACHE_LOCK_DIR=/var/lock/apache2\x00LANG=C\x00APACHE_RUN_USER=www-data\x00APACHE_RUN_GROUP=www-data\x00APACHE_LOG_DIR=/var/log/apache2\x00PWD=/var/www/html\x00']
```
An therefore we get the flag.

### Flag
Flag: flag{this_is_a_flag} (Change to desired flag)

## Distribution
No files to be distributed

### Credits
Google CTF - 2017

Misc.

Mindreader - 50pts
