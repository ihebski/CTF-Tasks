<?php



$directory = "./files";
$algo = 'sha512';
$title = '';
$secret = 'Y0uCant3ven5ue5sMY5ecritK3yItsHard!';

if(isset($_GET['algo'])){
	$algo = $_GET['algo'];
}

if(isset($_GET['file']) and isset($_GET['hash'])){
	if(hash($algo,$secret.$_GET['file'])==$_GET['hash']){
		$fileToGet = $directory."/".$_GET['file'];
		//Ugly hack to get this to work in PHP when it shouldn't due to null bytes. I feel dirty. (DC)
		$fileToGet = str_replace("\0",'',$fileToGet);
		$theData = nl2br(file_get_contents($fileToGet));
		$title = $_GET['file'];
	}
	else{
		header($_SERVER["SERVER_PROTOCOL"]." 404 Not Found"); 
		$title = "File not found";
		$header = $title;
	}
}else{
	$theData = "Please select an option from the left.";
}

?>
<html>
	<head>
		<title>Hack it 5! <?php print $title ?></title>
		 <link rel="stylesheet" type="text/css" href="style1.css" />
	</head>
	<body>
		<div id="header">
			<ul id="menu">
			<?php $files = glob("./files/*");
			foreach($files as $file){
				$fileName = basename($file);
				print "<li><a href=\"?file=".$fileName."&hash=".hash($algo,$secret.$fileName)."\"><span>".$fileName."</span></a></li>";
			}
			?>
			</ul>
		</div>


	




		<div id="content">
			<h1><?php print $title ?></h1>
	<?php print @$theData ?>
		</div>
</body>
</html>
