const Binary = require('./lib/binary');

let array = [1,2,3,5,9,10,6,125,12,15,100];

let bin = new Binary(array);

const res = bin.search(5);

console.log(res);