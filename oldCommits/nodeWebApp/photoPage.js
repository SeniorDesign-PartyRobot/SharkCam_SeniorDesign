const http = require('http');
var fs = require('fs')

const host = '127.0.0.1';
const port = 8080;




fs.readFile('./testHTML.html', function (error, html) {
    if (error) throw error;
    const server = http.createServer(function (request, response) {
        response.writeHeader(200, { "Content-Type": "text/html" });
        response.write(html);
        response.end();
    }).listen(port)
});