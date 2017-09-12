<?php
	include('configuration.php');

	if (isset($_POST['searchField'])) {
		$search = $_POST['searchField'];
		$search = str_ireplace('sleep', '', $search);
		$search = str_ireplace('benchmark', '', $search);
		$sql = "SELECT * FROM fish_shop WHERE name LIKE '%$search%' OR description LIKE '%$search%';";
		$retval = mysql_query($sql,$db);
		if(! $retval ) {
			die('Could not get data: ' . mysql_error());
		}
		while($row = mysql_fetch_array($retval, MYSQL_ASSOC)){
			echo "{$row['name']}<br>";
			echo "{$row['descrition']}<br>";
			echo "{$row['cost']}<br>";
			echo "{$row['image']}<br>";
			echo "{$row['id']}<br>";
		}
		mysql_close($db)
	} else {
		echo "<p>Nice try... But no.</p>";
	}
?>