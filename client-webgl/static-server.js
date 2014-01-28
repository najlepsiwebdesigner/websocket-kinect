  var fs = require("fs");
    var express = require("express");
    app = express.createServer();

    app.use(express.static(__dirname + '/'));
    app.get('/', function(req, res) {
        fs.readFile(__dirname + '/source.html', 'utf8', function(err, text){
            res.send(text);
        });
    });
    console.log('Server started on port 3000. Serving static files from /game/public directory.');
    app.listen(3000);