#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, res, content) {
  if (error) {
    console.error(error);
  }
  console.log('code: ' + res.statusCode);
});
