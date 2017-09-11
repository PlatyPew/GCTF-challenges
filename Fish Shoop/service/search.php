<?php
	include('configuration.php');

	if (isset($_POST['searchField'])) {
		$search = $_POST['searchField'];
		$search = str_ireplace('sleep', '', $search);
		$search = str_ireplace('benchmark', '', $search);
		$sql = "SELECT * FROM fish_shop WHERE name LIKE '%$search%' OR description LIKE '%$search%';";
	} else {
		echo "<p>Nice try... But no.</p>";
	}
?>