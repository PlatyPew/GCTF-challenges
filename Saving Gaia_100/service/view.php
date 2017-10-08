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
					putenv("Flag=GCTF{6l0b4l_w4rm1n6_15_r34lz}");
					$SECRET = "jNr19Dm9poBvz8zhPhjvzaRx72l4CNTRa3nHp1BshPOgtWLtu64vHQcuoBXD3VGXMeb8Eit5uyTQvTuGKjj2AH";
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
							echo exec("python read.py $file");
						} else {
							echo "You are not authorised to view this file!";
						}
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
