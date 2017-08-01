<?php
$toEncrypt = @$_GET['toEncrypt'];

function sToOrd($hashed){
$i=0;
$result= "";
$n = strlen(utf8_decode($hashed));
for ($i=0; $i < $n; $i++) { 
	$result .= ord($hashed[$i]);
}
return $result."00";}

function sumThat($aString){
	
	$first = (int) substr($aString, 0, 2);
	$seconde = (int) substr($aString, 2, 2);
	$third = (int) substr($aString, 3, 2);
	return $first + $seconde + $third;
}

function generate($ordred){
	$start = 0;
	$result= "";
	while ($start < 70) {
		$ch = substr($ordred, $start, 6);
		$hw = sumThat($ch);
		$k= $hw/8;
		$isIt = "display: inline-block;";
		if ($hw > 100) {
			$result .= "<div style='width:".$k."%;height:".$k."%;".$isIt."background:#".$ch."'></div>";
		}
	else	$result .= "<div style='width:".$k."%;height:".$k."%;background:#".$ch."'></div>";
		$start += 6;
	}
	return "<div style='height: 200px; width:300px;'>".$result."</div>";
}
if (preg_match('/[\'^£$%&*()}{@#~?><>,|=_+¬-]/', $toEncrypt))
{
    echo "Really ?";
}
else{
$hashed= md5($toEncrypt);

echo "<br>".generate(sToOrd($hashed));
}
?>