#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, response, body) {
    if (error) {
        console.log(error);
    }
    const data = JSON.parse(body);
    for (const character of data.characters) {
        request(character, function (error, response, body) {
            if (error) {
                console.log(error);
            }
            console.log(JSON.parse(body).name);
        });
    }
});
