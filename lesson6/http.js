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
                  fs.readFile("test.txt", 'utf-8', function (error, data) {
                              console.log(data);
                              res.writeHead(200, {
                                            'Content-Type': 'text/plain'
                                            });
                              if(!data){
                              var data = 0;
                              }
                              data = (parseInt(data) + 1);
                              var refresh = parseInt(data);
                              fs.writeFile('test.txt', parseInt(refresh).toString(), (error) => { /* handle error */ });
                              res.end('This page was refreshed ' + data + ' times!');
                              var data = "";
                              });
                  }).listen(8080);
