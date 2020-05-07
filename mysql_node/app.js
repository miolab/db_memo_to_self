const mysql = require('mysql');

const conn = mysql.createConnection({
  host : 'localhost',
  user : 'root',
  password : '',
  database : 'mydb_test',
  charset : 'utf8'
});

conn.connect( (err) => {
  if (err) throw err;
  console.log('Connected to MySQL...');
});

conn.query('select * from menu', (err, res) => {
  /* Expected Results
  [
    RowDataPacket { id: 1, name: 'math', score: 120.2, stars: 10 },
    RowDataPacket { id: 2, name: 'english', score: 88.1, stars: 8 },
    RowDataPacket { id: 3, name: 'physics', score: 90.5, stars: 8 }
  ]
  */
  if (err) throw err;
  console.log('Results: \n', res);
});

conn.end();

