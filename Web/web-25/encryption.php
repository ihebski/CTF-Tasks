<?php if($_SERVER['HTTP_USER_AGENT'] === 'Bugs_Bunny Browser'){setcookie("flag", "zn8XhqnlBRBetevoFcSQAw0OMVH6Kwj23svbneF1+5gDfBdn9osZBfB06cTub4ARg3OTTjsBIG7x", time()+100, $_SERVER['REQUEST_URI'], $_SERVER['SERVER_NAME']);}?>
<!DOCTYPE html>
<html lang="EN">
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>encryption</title>

	</head>
	<body>
		<h1 class="text-center">Welcome to bugs_bunny CTF</h1>
		<?php if ($_SERVER['HTTP_USER_AGENT'] !== 'Bugs_Bunny Browser'):?>
		<div class="alert alert-danger" role="alert">Error: Unauthorized browser <?php echo  $_SERVER['HTTP_USER_AGENT'].' detected.<br>Only users of "Bugs_Bunny Browser" may access this page.'; ?></div>
		<?php endif ?>
		<?php if ($_SERVER['HTTP_USER_AGENT'] === 'Bugs_Bunny Browser'):?>
			
			<div class="alert alert-info" role="alert">Good Job! but this is only the step 1/2<br>This is your key maybe you need it "Hashkiller"</div>
		<?php endif ?>
		<!-- jQuery -->
		
	</body>
</html>