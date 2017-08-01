// Express initialization
var express = require('express');
var bodyParser = require('body-parser');
var app = express();
app.use(bodyParser());
app.set('title', 'Score Center');
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/test";

MongoClient.connect(url, function(err, databaseConnection) {
  console.log("[+] Database UP !");
  db = databaseConnection;
})
app.use(express.static(__dirname + '/css'));

app.get('/', function(request, response) {
  console.log("[+] application UP !");
  response.set('Content-Type', 'text/html');
  var indexPage = '';
  db.collection('scores', function(er, collection) {
    collection.find().sort({
      score: -1
    }).limit(100).toArray(function(err, cursor) {
      if (!err) {
        indexPage += "<!DOCTYPE html><html><head> <title>Score Center</title> <meta name='author' content='sold1er' /> </head><body> <div id='page'> <div id='logo'> <h1><a href='/' id='logoLink'>Score Center</a></h1> </div> <div id='nav'> <ul> <li><a href='#/home.html'>Home</a></li> <li><a href='#/about.html'>About</a></li> <li><a href='#/contact.html'>Contact</a></li> </ul> </div> <div id='content'> <p> I have created an application to save my team score and grid ,Alex and my score are stored </p> <p> My friend said that he has hacked my application and got the flag !! ,Please helps me to figure out how he did it !! </p> <p> <a href='http://localhost:5001/scores.json?username=Denni&uid=2583'>My Score</a> <br> <a href='http://localhost:5001/scores.json?username=alex&uid=1141'>Alex Score</a> </p> </div> <div id='footer'> <p> Service powered with <a href='/' target='_blank'>Nodejs</a> </p> </div> </div></body></html><style type='text/css' media='screen'>/** multi-line comment*/p{ line-height: 1em; }h1, h2, h3, h4{ color: orange; font-weight: normal; line-height: 1.1em; margin: 0 0 .5em 0;}h1{ font-size: 1.7em; }h2{ font-size: 1.5em; }a{ color: black; text-decoration: none;} a:hover, a:active{ text-decoration: underline; }/* you can structure your code's white space so that it is as readable for when you come back in the future or for other people to read and edit quickly */body{ font-family: arial; font-size: 80%; line-height: 1.2em; width: 100%; margin: 0; background: #eee;}/* you can put your code all in one line like above */#page{ margin: 20px; }/* or on different lines like below */#logo{ width: 35%; margin-top: 5px; font-family: georgia; display: inline-block;}/* but try and be as concise as possible */#nav{ width: 60%; display: inline-block; text-align: right; float: right;} #nav ul{} #nav ul li{ display: inline-block; height: 62px; } #nav ul li a{ padding: 20px; background: orange; color: white; } #nav ul li a:hover{ background-color: #ffb424; box-shadow: 0px 1px 1px #666; } #nav ul li a:active{ background-color: #ff8f00; }#content{ margin: 30px 0; background: white; padding: 20px; clear: both;}#footer{ border-bottom: 1px #ccc solid; margin-bottom: 10px;} #footer p{ text-align: right; text-transform: uppercase; font-size: 80%; color: grey; }/* multiple styles seperated by a , */#content,ul li a{ box-shadow: 0px 1px 1px #999; }</style>"

        response.send(indexPage);


      } else {

        response.send('<!DOCTYPE HTML><html><head><title>ScoreCenter</title></head><body><h1>Whoops, something went terribly wrong!</h1></body></html>');

      }
    });
  });
});

app.post('/submit.json', function(request, response) {
  // Enabling CORS
  response.header("Access-Control-Allow-Origin", "*");
  response.header("Access-Control-Allow-Headers", "X-Requested-With");

  var username = request.body.username;
  var score = parseInt(request.body.score);
  var uid = request.body.uid;
  var grid = request.body.grid;
  if (username != undefined && score != undefined && grid != undefined && uid != undefined) {
    var toInsert = {
      "username": username,
      "score": score,
      "grid": grid,
      "created_at": Date(),
      "uid": uid
    };
    db.collection('scores', function(er, collection) {
      var id = collection.insert(toInsert, function(err, saved) {
        if (err) {
          response.send(500)
        } else if (!saved) {
          response.send(500);
        } else {
          response.send(200);
        }
      });
    });
  }
  else {
    response.send("Data did not go through");
  }
});

app.get('/scores.json', function(request, response) {
  // Enabling CORS
  response.header("Access-Control-Allow-Origin", "*");
  response.header("Access-Control-Allow-Headers", "X-Requested-With");

  var u_username = request.query.username;
  var o_id = request.query.uid;    
  console.log(o_id); 
  console.log(u_username); 
  if (request.query.username === undefined) {
    response.send("[]");
  } else {
    db.collection('scores', function(er, collection) {
      collection.find(
        {"username":u_username,"uid":o_id}
        ).sort({
        score: -1
      }).limit(10).toArray(function(err, docs) {
        //console.log(docs);
        response.send(JSON.stringify(docs));
      });
    });
  }
});

app.listen(process.env.PORT || 5001);