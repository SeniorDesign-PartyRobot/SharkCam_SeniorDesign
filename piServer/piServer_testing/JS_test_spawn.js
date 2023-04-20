const { spawn } = require('child_process');

var data1;
const process = spawn('python', ['python_test_spawn.py']);
process.stdout.on('data', function (data) {
    console.log("Data from python script");
    data1 = data.toString();
    console.log(data1);
});