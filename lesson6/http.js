var http = require("http"),
fs = require("fs");
http.createServer(function (request, response) {
                  fs.readFile("test.txt", 'utf-8', function (error, data) {
                              console.log(data);
                              response.writeHead(200, {
                                                 'Content-Type': 'text/plain'
                                                 });
                              if(!data){
                              var data = 0;
                              }
                              data = (parseInt(data) + 1);
                              var refresh = parseInt(data);
                              fs.writeFile('test.txt', parseInt(refresh));
                              response.end('This page was refreshed ' + data + ' times!');
                              var data = "";
                              });
                  }).listen(8080);
