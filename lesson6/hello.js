var http = require('http');
var path = require('path');
var fs = require('fs');
var url = require('url');
var favicon = path.join(__dirname, 'static', 'favicon.ico');

http.createServer(function (req, res) {
                  var pathname = url.parse(req.url).pathname;
                  if (req.method === 'GET' && pathname === '/favicon.ico') {
                    res.setHeader('Content-Type', 'image/x-icon');
                    fs.createReadStream(favicon).pipe(res);
                    return;
                  }
                  req.on('end', function () {
                         console.log('request end event fired');
                         });
                  res.writeHead(200, {'Content-Type': 'text/plain'});
                  res.end('Hello World!\n');
                  console.log('response end call done');
                  }).listen(8080);

console.log('Server running at http://127.0.0.1:8080/');
