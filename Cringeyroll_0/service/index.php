<!DOCTYPE HTML>
<html>
	<head>
		<title>Anime Awards</title>
	</head>
	<body>
		<section>
			<h1>Anime Awards</h1>
			<p>Give a score to the following anime</p>
		</section>
		<section>
			<h2>Sword Art Online</h2>
			<article>
				<h3>Reviews</h3>
				<p>BEST ANIME EVAR 10/10</p>
				<p>KIRITO-KUN!!!</p>
				<p>Your taste in anime is equivalent to that of my excrements</p>
			</article>
			<article>
				<h3>Score</h3>
				<p><?php echo 200 + $_POST["sao"];?> points</p>
			</article>
			<form action="index.php" method="POST">
				<h3>Rate</h3>
				<select name="sao">
					<option value="1">1</option>
					<option value="2">2</option>
					<option value="3">3</option>
					<option value="4">4</option>
					<option value="5">5</option>
					<input type="submit" value="Submit">
				</select>
			</form>
		</section>
		<section>
			<h2>Naruto</h2>
			<article>
				<h3>Reviews</h3>
				<p>Naruto btr thn any anime!11!11!!!</p>
				<p>Why are there so many Narutards?</p>
			</article>
			<article>
				<h3>Score</h3>
				<p><?php echo 500 + $_POST["naruto"];?> points</p>
			</article>
			<form action="index.php" method="POST">
				<h3>Rate</h3>
				<select name="naruto">
					<option value="1">1</option>
					<option value="2">2</option>
					<option value="3">3</option>
					<option value="4">4</option>
					<option value="5">5</option>
					<input type="submit" value="Submit">
				</select>
			</form>
		</section>
		<section>
			<h2>Dragon Ball Z</h2>
			<article>
				<h3>Reviews</h3>
				<p>Goku can beat anyone. Come fight me 1 on 1 bro!</p>
				<p>ausdyga,dgsusgyad,kyugsjad</p>
			</article>
			<article>
				<h3>Score</h3>
				<p><?php echo 9001 + $_POST["dbz"];?> points</p>
			</article>
			<form action="index.php" method="POST">
				<h3>Rate</h3>
				<select name="dbz">
					<option value="1">1</option>
					<option value="2">2</option>
					<option value="3">3</option>
					<option value="4">4</option>
					<option value="5">5</option>
					<input type="submit" value="Submit">
				</select>
			</form>
		</section>
		<section>
			<h2>Yuri On Ice</h2>
			<article>
				<h3>Reviews</h3>
				<p>This show is bad</p>
			</article>
			<article>
				<h3>Score</h3>
				<p><?php $value = -200 + $_POST["yoi"]; echo $value; ?> points</p>
				<?php
					if ($value === 1000000) {
						echo "<p>GCTF{7h3_4n1m3_4w4rd5_w3r3_r1663d}</p>";
					}
				?>
			</article>
			<form action="index.php" method="POST">
				<h3>Rate</h3>
				<select name="yoi">
					<option value="1">1</option>
					<option value="2">2</option>
					<option value="3">3</option>
					<option value="4">4</option>
					<option value="5">5</option>
					<input type="submit" value="Submit">
				</select>
			</form>
		</section>
	</body>
</html>