<!DOCTYPE HTML>
<?php
	include("configuration.php");
	$search = $_GET["search"];
	if ($search === "") {
		$search = "qwertyuiop";
	}
	$search = str_ireplace('sleep', '', $search);
	$search = str_ireplace('benchmark', '', $search);
	try {
		if ($conn->connect_error) {
			die("Connection failed: " . $conn->connect_error);
		}
		$query = "SELECT * FROM fish_shop WHERE name LIKE '%$search%';";
		$result = $conn->query($query);
		if (!$result) {
			$error = mysqli_error($conn);
		} else {
			while ($row = $result->fetch_assoc()) {
				$output .= "<tr style=\"font-size:20px\"><td>" . $row["name"] . "</td>";
				$output .= "<td>" . $row["description"] . "</td>";
				$output .= "<td><img src=\"" . $row["image"] . "\" width=200px></td>";
				$output .= "<td>$" . $row["cost"] . "</td></tr>";
			}
		}
	} catch (Exception $e) {
		echo $e->getMessage();
	}
?>
<html>

<head>
	<title>Fish Shoups</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>

<style>
.btn-default {
	margin-left: 70px
}
</style>

<body style="background-color:#F8F8F8;">

	<div class="container">
		<h2>Search Fishes</h2>
		<p>De beautifool fishes that swims like humans!! Buy them today!!!!! Never on sale because where else can you find fishes that shit marshmellows and burp rainbows. Rainbows are good for health!</p>
		<p>The world is good for your health! Buy the fishes and the huat will be with you!!! HUAT AH!!!!! XIN NIAN KUAI LE!!!!!!! Buy the fishes and be happy for all your life!!!!!</p>
		<form action method="GET">
		<input type="text" class="form-control" name="search" placeholder="Search" style="width:80%;">
		<input type="submit" class="btn btn-success" value="submit">
	</form>
	<br>
	<div class="table-responsive">
			<table class="table">
				<thead>
					<tr>
						<th>Name</th>
						<th>Description</th>
						<th>Image</th>
						<th>Price</th>
					</tr>
				</thead>
				<tbody>
					 <?php echo $output; ?>
				</tbody>
			</table>
		</div>
	</div>
	<button  class="btn btn-default" onclick="location.href='index.html'">Back to home</button>
<?php
	echo $error;
?>
<br>
<br>
<br>
</body>
</html>
