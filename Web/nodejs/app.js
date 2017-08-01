var express = require('express');
var bodyParser     =        require("body-parser");
var exec = require('child_process').exec, child;

var app = express();
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.use(express.static('public'))
var path  = require("path");
var pattern =/[a-zA-Z@\"\'&<>:;_{}.$^~#|-~]+/g;
var PORT = 1994;

app.get('/', function (req, res) {
  res.sendFile('index.html', {root: __dirname })
});
app.post('/calcule',function (req,res) {
	//console.log(req.body.data.match(pattern));
	if(req.body.data.match(pattern)){
		res.send('only "1-9 []()/*-+!" accepted');
	}else{
		child = exec('node getflag.js "'+req.body.data+'"',
	  		function (error, stdout, stderr) {
	  			if(stdout!== ''){
	  				res.send(stdout);
	  			}else{
	  				res.send(req.body.data);
	  			}
	    		console.log(req.body.data);
			console.log('stdout '+ stdout);
			console.log('=======================================================');
	    	//	console.log('stderr: ' + stderr);
	   		 if (error !== null) {
	      	//	console.log('exec error: ' + error);
	   			 }
			});
				
	}
	
});
app.listen(PORT, function () {
  console.log('Server listen on port ' + PORT)
})
