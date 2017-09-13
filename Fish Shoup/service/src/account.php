<!DOCTYPE HTML>
<?php
	include("configuration.php");
	$user = $_GET[ "user"];
	$password = $_GET["password"];
	try {
		if ($conn->connect_error) {
			die("Connection failed: " . $conn->connect_error);
		}
		$query = "SELECT * FROM user_details_login WHERE user = ? AND password = ?;";
		$stmt = $conn->prepare($query);
		$stmt->bind_param("ss",$user,$password);
		$stmt->execute();
		$stmt->store_result();
		$stmt->bind_result($usr, $pwd, $role);
		$k = 0;
		while($stmt->fetch()) {
			$k = 1;
		}
		$stmt->close();
	} catch (Exception $e) {
		 echo $e->getMessage();
	}
?>
<html lang="en">
	<head>
		<title>Fish Shoups</title>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
		<style>
			/* Set height of the grid so .sidenav can be 100% (adjust if needed) */
			.row.content {
				height: 1500px
			}
			/* Set gray background color and 100% height */
			.sidenav {
				background-color: #f1f1f1;
				height: 100%;
			}
			/* Set black background color, white text and some padding */
			footer {
				background-color: #555;
				color: white;
				padding: 15px;
			}
			/* On small screens, set height to 'auto' for sidenav and grid */
			@media screen and (max-width: 767px) {
				.sidenav {
					height: auto;
					padding: 15px;
				}
				.row.content {
					height: auto;
				}
			}
		</style>
	</head>
	<body>
		<div class="container-fluid">
			<div class="row content">
				<div class="col-sm-3 sidenav">
					<h4>WELCOME TO DE FISH HOMIE</h4>
					<button  class="btn btn-default" onclick="location.href='index.html'">Back to home</button>
					<br>
				</div>
				<div class="col-sm-9">
					<h4><small>RECENT POSTS</small></h4>
					<hr>
					<h2>I Love Food</h2>
					<h5><span class="glyphicon glyphicon-time"></span> Post by Molly Mouth, Bisheu 27, 2015.</h5>
					<h5><span class="label label-danger">Food</span> <span class="label label-primary">Worms</span></h5>
					<br>
					<p>Food is my passion. I only live to eat. Food lives for me. Worms lives for me. Worms are bae. Can you feel my love tonight? They say obsession is bad but I AM BADLY - NO! TERRIBLY obsessed with de wormos. Can I please have worms for lunch again? Imma go to the fish pilgrimage to hope for more worms that magically appear on hooks tomorrow. This is me below!</p>
					<img src="image/mouthy.jpg" class="img-responsive" style="width:100%" alt="Image">
					<br>
					<br>
					<h4><small>RECENT POSTS</small></h4>
					<hr>
					<h2>HIrows!</h2>
					<h5><span class="glyphicon glyphicon-time"></span> Post by Boolabala, Febooahris 24, 2015.</h5>
					<h5><span class="label label-success">Enlish</span></h5>
					<br>
					<p>BOolablla iz de veries scardies and sadies!!! Me is enlish noobes! I thenks mi Enlisheu iseu veries de bagusly goodies! I hasves nos ideasd whades iz wronges wifes mi Enlish!!! I is A veries sades fisheu :( Hellpoos mi! Whye de nos ones gets mi. I alsos wants tos goes marshmellows burpinz wifo frewins!!! I ams many de jellos of manies of fisheus. I wnas frinds or amz mi justzs too uglies? Thiz ise mes belrows!!!</p>
					<img src="image/ballons.jpg" class="img-responsive" style="width:50% height:50%" alt="Image">
					<hr>
				</div>
			</div>
		</div>

		<footer class="container-fluid">
			<p>Disclaimer: If you ever tell any living or dead soul about this YOU ARE A DEAD HUMAN! Unless you are a fish, in the Law of Fishshoup Section 100, it states that you will have to eat clams in your entire fish life! So telling is a no-no.</p>

<?php
if ($k === 0) {
	header("Location: login.html");
	die();
} else {
	if ($role === "admin") {
		echo "<p>Just because he's the admin doesn't mean he has the flag!</p>";
	} else if ($usr === "Merrkat") {
		echo "<p>GCTF{m00ny_607_17}</p>";
	}
}
?>
                </footer>
        </body>
</html>

