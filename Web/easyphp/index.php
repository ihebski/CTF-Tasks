<?php
require("secret.php");
$flag= $secret; // for test
$admin = "admin"; //for test
function auth($user,$admin,$password, $flag){
    $res=0;
    if ( isset($user)&& $user !="" &&isset($password) && $password!=""){
        if ( $password == $flag && $user == $admin ){
            $res=1;
        }
    }
    $_SESSION["logged"]=$res;
    return $res;
}



function display($res){
    $aff= '
    <!DOCTYPE html>
    <html >
    <head>
      <meta charset="UTF-8">
      <title>Admin login</title>
    
          <link rel="stylesheet" href="style.css">
    </head>
    
    <body>  
    <form action="" method="POST">
      <header>Login</header>
      <label>Username <span>*</span></label>
      <input type="text" name="user"/>
      <div class="help">At least 6 character</div>
      <label>Password <span>*</span></label>
      <input type="password" name="password"/>
      <div class="help">Use upper and lowercase lettes as well</div>
      <button type="submit" value="login" >Login</button>
	<h3>'.htmlentities($res).'</h3>
    </form>     
      
    </body>
    </html>';
    return $aff;
}



session_start();
if ( ! isset($_SESSION["logged"]) )
    $_SESSION["logged"]=0;

$aff="";
#include("config.inc.php");

if (isset($_POST["password"]))
    $password = $_POST["password"];

if (isset($_POST["user"]))
    $user = $_POST["user"];

if (!ini_get('register_globals')) {
    $superglobals = array($_SERVER, $_ENV,$_FILES, $_COOKIE, $_POST, $_GET);
    if (isset($_SESSION)) {
        array_unshift($superglobals, $_SESSION);
    }
    foreach ($superglobals as $superglobal) {
        extract($superglobal, 0 );
    }
}

if (( isset ($user) && $user!= ""  && isset ($password) && $password!="" && auth($user,$admin,$password,$flag)==1) || (is_array($_SESSION) && $_SESSION["logged"]==1 ) ){
    $aff=display("well done, you can validate with the password : $flag");
} else {
    $aff=display("try again");
}

echo $aff;

?>

