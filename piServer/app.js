const express = require("express");
const app = express();
const http = require("http");
const WebSocket = require("ws");
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });
const port = 3000;
const { spawn } = require('child_process');

var data1;
const process = spawn('python', ['python_test_spawn.py']);
process.stdout.on('data', function (data) {
    console.log("Data from python script");
    data1 = data.toString();
    console.log(data1);
});

wss.on("connection", function connection(ws) {
    console.log('New connection');
    ws.send('howdy');
    var incomingMsg;
    ws.on('message', (data) => { // this loops forever. Why?
        incomingMsg = data.toString();
        if (incomingMsg == 'start') {
            console.log("start message received");

        }
        if (incomingMsg == 'stop') {
            console.log("stop message received");
        } else {
            console.log(incomingMsg);
        }
    });
    ws.onclose = (e) => {
        console.log("connection closed");
    }
});


server.listen(8080, () => {
    console.log("Listening to port 8080");
});

