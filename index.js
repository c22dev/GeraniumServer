
const http = require('http');
const fs = require('fs');

const server = http.createServer((req, res) => {
  if (req.method === 'POST') {
    let data = '';
    req.on('data', chunk => {
      data += chunk;
    });

    req.on('end', () => {
      const randomString = Math.random().toString(36).substring(7);
      const filename = `data_${randomString}.txt`;
      fs.writeFile(filename, data, (err) => {
        if (err) throw err;
        console.log(`Data saved to ${filename}`);
      });

      res.end('SUCCESS');
    });
  } else {
    res.end('Geranium Log Server v0.1. Output : Invalid request.');
  }
});
server.listen(3000, () => {
  console.log("Geranium Log Server v0.1")
  console.log("made by c22dev")
  console.log("")
  console.log("This was made for Geranium. Geranium itself is under GPLv3 license. The license also apply to the log server.")
});