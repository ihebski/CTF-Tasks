<?php
error_reporting(0);

$flag = "";
if (@$_GET['password'] &&  @$_GET['username']){

    $db = new SQLite3('sqli_f.db');


    $pass = (@$_GET['password']);
    $user = (@$_GET['username']);
    if(preg_match('/(and|or|union|limit|where)/i', $user))
       exit('No way SOrry');
    if(preg_match('/\s/', $pass)) 
      exit('No way SOrry');
    if(preg_match('/(username)/i', $pass))
       exit('No way SOrry');

    $result = $db->query("SELECT username FROM USERS WHERE username='$user' and password='$pass'");
    if($res = $result->fetchArray()){
        if(!isset($res['username'])) continue;
        $flag =  $res['username'];
    }
}

?>


<!DOCTYPE html>
<html>

<head>

  <meta charset="UTF-8">

  <title>SQLI-F - Log-in</title>

  <link rel='stylesheet' href='http://codepen.io/assets/libs/fullpage/jquery-ui.css'>

    <link rel="stylesheet" href="css/style.css" media="screen" type="text/css" />

</head>

<body>

  <div class="login-card">
    <h1>Log-in</h1><br>
  <form method="GET" action="">
    <input type="text" name="username" placeholder="Username">
    <input type="password" name="password" placeholder="Password">
    <input type="submit" name="login" class="login login-submit" value="login">
  </form>

  <div class="login-help">
    <p> <?php echo $flag; ?></p>
  </div>
</div>

  <script src='http://codepen.io/assets/libs/fullpage/jquery_and_jqueryui.js'></script>

</body>

</html>
