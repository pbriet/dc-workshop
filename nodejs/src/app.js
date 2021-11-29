const express = require("express");
const app = express();
const mysql = require('mysql');

const connection = mysql.createConnection({
  host     : process.env.MYSQL_HOST,
  user     : process.env.MYSQL_USER,
  password : process.env.MYSQL_PASSWORD,
  database : process.env.MYSQL_DATABASE
});

connection.connect((err) => {
    if(err) throw err;
    console.log('Connected to MySQL Server!');
});

app.get("/",(req,res) => {
    connection.query('SELECT version()', (err, rows) => {
        if(err) throw err;
        console.log('Version is: \n', rows);
        res.send('Version is : ' + rows[0]['version()'])
    });
});

app.listen(3000, () => {
    console.log('Server is running at port 3000');
});