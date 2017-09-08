<html>
	<head>
		<title>COOKIE MONSTER's iMaGe ViEwEr</title>
	</head>
	<body background="https://pbs.twimg.com/profile_images/552145045663408129/egywNuyx.png">
		<?php
			$url = htmlentities($_GET["url"]);
		?>
		<div>
			<h1>HeRe Is YoUr ImAgE!</h1>
			<img src='<?php echo $url ?>' width="500">
			<p><h2>Thank you for using image viewer</h2></p>
			<p>Image source : <?php echo $url ?></p>
		</div>
	</body>
</html>
