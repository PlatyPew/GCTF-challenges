<?php

   	include("config.php");

	$user = $_GET["user"];
	$password = $_GET["password"];

   	$stmt = $conn->prepare("SELECT user, password FROM user_details_login WHERE 'user' = ? AND 'password' = ?;");
	$stmt->bind_param("ss", $user, $password);
	$stmt->execute();

	$result = mysqli_query($db,$sql);
	$count = mysqli_num_rows($result);

	while ($row = mysqli_fetch_array($result,MYSQLI_NUM)) {
		$output .= "{$row['user']} {$row['password']}";
	}

	$stmt->close();
	$conn->close();
?>
<html>
	<head>
		<title>Fish Shoop</title>
	</head>
	<body>
		<?php
			echo "$output<br>"
		?>
	</body>
</html>