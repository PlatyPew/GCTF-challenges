<html>
	<head>
		<title>Saving Gaia</title>
	</head>
	<body>
		<h2>Here are our proud supporters!</h2>
		<?php
			putenv("Flag=flag{this_is_a_flag}");
			$SECRET = "YvrL1KbyV8VPUneie2M7";
			$file = $_POST["file"];
			$mac = $_POST["mac"];
			$file = pack("H*",$file);
			$hash = hash("sha1",$SECRET.$file);
			$file = explode(",",$file);
			$file = $file[sizeof($file)-1];
			if ($hash === $mac) {
				echo exec("python read.py $file");
			} else {
				echo "You are not authorised to view this file!";
			}
		?>
		<br>
		<p>Save the environment to get the flag!</p>
		<a href="index.html">Go back</a>
	</body>
</html>
