<?php
$toEncrypt = @$_GET['toEncrypt'];


function sToOrd($toEncrypt, $n){
$i=0;
$result= "";
for ($i=0; $i < $n; $i++) { 
	$result .= ord(strtoupper($toEncrypt[$i]));
}
return $result;}


function randomPick ()
{
	$i=0;
	$result="";
	for ($i=0; $i <8 ; $i++) { 
		$x=rand (2,9);
		$result.= $x;
	}
return $result;
}


function counterPick ($randomNumber){
	$i=0;
	$result="";

	for ($i=0; $i <8 ; $i++) { 
		$var = (int)$randomNumber[$i];
		$diff = 9 - $var;
		$result.=$diff;
	}
	return $result;
}


function sumThem ($ordred)
{
	$keyOne = randomPick();
	$decKeyOne= counterPick($keyOne);

	$keyTow = randomPick();
	$decKeyTow= counterPick($keyTow);

	$keyThr = randomPick();
	$decKeyThr= counterPick($keyThr);
	

	$n = strlen(utf8_decode($ordred));

	if ($n < 8) 
		{
			$diffLength = 8 - $n;
			$newLength = $diffLength + $n;
		  	$i=0;
		  	for ($i=$n; $i < $newLength ; $i++) 
		  	{ 
		  		$ordred .='0';
		  	}

		}

		$var = (int) $ordred;
		$keyOneConv = (int)$keyOne;		$decKeyOneConv = (int)$decKeyOne;
		$keyTowConv = (int)$keyTow;		$decKeyTowConv = (int)$decKeyTow;
		$keyThrConv = (int)$keyThr;		

		$preFinalEncrypted = $keyOneConv + $decKeyOneConv + $keyTowConv + $decKeyTowConv + $keyThrConv + $var;

		$tmp = (string) $preFinalEncrypted;
		$i = 0;
		$finalEncrypted="";
	//	echo '*'.$preFinalEncrypted.'* <br> *'.$decKeyThr.'* <br>';
		for ($i=0; $i < 8; $i++) { 
			$finalEncrypted .= $tmp[$i].$decKeyThr[$i];
		}
		$finalEncrypted.=$tmp[8];
return $finalEncrypted;
}

function recrypt ($ordred){
	$n = strlen(utf8_decode($ordred));
	$repeat = $n/8;
	$i=0;
	$ch= "";
	$start = 0; 
	for ($i=0; $i < $repeat ; $i++) {
		
			if ($n - $start < 8) {
				$ch = substr($ordred, $start, $n%8);
				echo sumThem($ch).'*';
				}
			else {$ch	= substr($ordred, $start, 8);
				$start +=8;
				echo sumThem($ch).'*';
				}
	}
}

// main

if (preg_match('/[\'^£$%&*()}{@#~?><>,|=_+¬-]/', $toEncrypt))
{
    echo "WTF ? we encrypt Strings here babe :) WP anyway... no codes please, only characters";
}
else{
$n = strlen(utf8_decode($toEncrypt));
$orded = sToOrd($toEncrypt, $n);
echo recrypt($orded);
}
?>