const express = require('express');
const bodyParser = require('body-parser');
const { MongoClient } = require('mongodb');
const app = express();

// Database connection URL
const url = 'mongodb://localhost:27017';
const dbName = 'student_db';

// Middleware to serve static files (for HTML form)
app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: true }));

// Connect to MongoDB
MongoClient.connect(url, { useUnifiedTopology: true }, (err, client) => {
  if (err) throw err;
  console.log('Connected to MongoDB');
  const db = client.db(dbName);

  // Handle form submission
  app.post('/register', (req, res) => {
    const student = {
      student_id: req.body.student_id,
      name: req.body.name,
      email: req.body.email,
      age: req.body.age,
      course: req.body.course,
      registration_date: new Date()
    };

    db.collection('students').insertOne(student, (err, result) => {
      if (err) throw err;
      console.log('Student registered:', result);
      res.send('Student registered successfully!');
    });
  });

  // Start the server
  app.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
  });
});
