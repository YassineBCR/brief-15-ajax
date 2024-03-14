const http = require('http');
const fs = require('fs');
const port = 8001;

const server = http.createServer((req, res) => {
  fs.readFile('index.html', 'utf-8', (err, content) => {
    if (err) {
      res.writeHead(500);
      res.end('Error: ' + err);
    } else {
      res.writeHead(200, { 'Content-Type': 'text/html' });
      res.end(content);
    }
  });
});

server.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});