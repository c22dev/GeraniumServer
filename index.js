const http = require('http');

const server = http.createServer((req, res) => {
  if (req.method === 'POST') {
    let data = '';
    req.on('data', chunk => {
      data += chunk;
    });

    req.on('end', () => {
      console.log(`${data}`);
      res.end('SUCCESS');
    });
  } else {
    res.end('Geranium Log Server v0.2. Output : Invalid request.');
  }
});

server.listen(3000, () => {
  console.log("Geranium Log Server v0.1");
  console.log("made by c22dev");
  console.log("");
  console.log("This was made for Geranium. Geranium itself is under GPLv3 license. The license also applies to the log server.");
  console.log("");
  console.log("");
});
