const http = require('http');

const server = http.createServer((req, res) => {
  if (req.method === 'POST') {
    let data = '';
    req.on('data', chunk => {
      data += chunk;
    });

    req.on('end', () => {
      res.end('SUCCESS');
    });
  } else {
    res.end('Geranium Log Server v0.3. Invalid request.');
  }
});

server.listen(3000, () => {
  console.log("Geranium Log Server v0.3");
  console.log("made by c22dev");
  console.log("");
  console.log("This was made for Geranium. Geranium itself is under GPLv3 license. The license also applies to the log server.");
});
