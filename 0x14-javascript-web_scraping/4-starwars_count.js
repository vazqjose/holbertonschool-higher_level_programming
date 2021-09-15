#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const id = '18';
let count = 0;

request(url, function (error, response, body) {
	if (error) {
		console.error(error);
	}
	movies = JSON.parse(body).results;

	for (let j = 0; j < movies.length; j++) {
		let list = movies[j].characters;

		for (let i = 0; i < list.length; i++) {
			request(list[i], function (errorB, resB, contentB) {
				if (errorB) {
					console.error(errorB);
				}
				charName = JSON.parse(contentB).name;
				if (charName == "Wedge Antilles") {
					count++;
					console.log(count);
				}
				console.log(movie);
			}); // request
		}
	}
});
