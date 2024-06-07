#!/usr/bin/node

const request = require('request');

const out = []
request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], function (error, response, body) {
    if (error) {
        console.log(error);
    }
    const data = JSON.parse(body);
    fetchCharacters(data.characters, 0);
});

function fetchCharacters (characters, index) {
    request(characters[index], function (error, response, body) {
        if (error) {
            return
        }
        console.log(JSON.parse(body).name);
        if (index < characters.length - 1) {
            fetchCharacters(characters, index + 1);
        }
    });
}
