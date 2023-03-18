const express = require("express");
const app = express();
const http = require("http");
const WebSocket = require("ws");
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

wss.on("connection", function connection(ws) {
    console.log('New connection');
    ws.send('howdy');

});

app.get("/", (req, res) => {
    res.send("Hello World!");
});
server.listen(8080, () => {
    console.log("Listening to port 8080");
});