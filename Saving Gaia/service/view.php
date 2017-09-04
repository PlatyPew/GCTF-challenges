<html>
	<head>
		<title>Saving Gaia</title>
		<link rel = "stylesheet" type = "text/css" href ="gaia.css">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
	</head>
	<body>
		<section>
			<img src="gaia.jpg" width=100% class="img-fluid" alt="Save my world">
		</section>
		<section id="section1">
			<h2>Here are our proud supporters!</h2>
			<article>
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
			</article>
			<br>
			<p>Save the environment to get the flag!</p>
			<p><a href="index.html">Go back</a></p>
		</section>
		<footer class="container-fluid">
			<p>&copy; Saving Gaia &bull; GCTF</p>
		</footer>
	</body>
</html>
