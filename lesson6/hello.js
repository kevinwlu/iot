var http = require('http');

http.createServer(function (request, response) {
                  request.on('end', function () {
                             console.log('request end event fired');
                             });
                  response.writeHead(200, {'Content-Type': 'text/plain'});
                  response.end('Hello World!\n');
                  console.log('response end call done');
                  }).listen(8080);

console.log('Server running at http://127.0.0.1:8080/');
