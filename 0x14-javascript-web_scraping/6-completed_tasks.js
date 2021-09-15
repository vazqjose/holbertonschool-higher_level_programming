#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const url = 'https://jsonplaceholder.typicode.com/todos';

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  });
});
