#!/usr/bin/node

const fiRst = process.argv[2];

console.log(isNaN(fiRst) ? 'Not a number' : 'My number: ' + fiRst);
