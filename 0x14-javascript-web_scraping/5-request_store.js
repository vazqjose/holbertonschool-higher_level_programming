#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const file = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  fs.writeFile(file, body, 'utf-8', (err) => {
    if (err) {
      console.error('error:', err);
    }
  });
});
