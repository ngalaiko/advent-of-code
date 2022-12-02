const input = require("fs")
  .readFileSync("./input.txt", "utf8")
  .toString();

const testInput = require("fs")
  .readFileSync("./test.txt", "utf8")
  .toString();

const binaryToArray = string => {
  let charArray = [];
  for (let i = 0; i < string.length; i++) {
    if (string[i] === "0") {
      charArray.push(0);
    } else {
      charArray.push(1);
    }
  }
  return charArray;
};

const rows = input
  // const rows = testInput
  .split("\n")
  .filter(s => s.length > 0)
  .map(binaryToArray);

const sumArrayIndices = (a1, a2) => {
  let sum = [];
  for (let i = 0; i < a1.length; i++) {
    sum.push(a1[i] + a2[i]);
  }
  return sum;
};

const countGamma = (counts, total) => {
  return counts.map(c => (c >= total / 2 ? 1 : 0));
};

const countEpsilon = (counts, total) => {
  return counts.map(c => (c >= total / 2 ? 0 : 1));
};

const f = (counts, pos) => {
  return binary => {
    return binary[pos] == counts[pos];
  };
};

let ogRows = rows;
for (let i = 0; ogRows.length != 1; i++) {
  const onesCount = ogRows.slice(1).reduce(sumArrayIndices, ogRows[0]);
  const mostCommonBits = countGamma(onesCount, ogRows.length);

  ogRows = ogRows.filter(f(mostCommonBits, i));
}

let co2 = rows;
for (let i = 0; co2.length != 1; i++) {
  const onesCount = co2.slice(1).reduce(sumArrayIndices, co2[0]);
  const leastCommonBits = countEpsilon(onesCount, co2.length);

  co2 = co2.filter(f(leastCommonBits, i));
}

const convertBinaryToDecimal = binary => {
  let decimal = 0;
  let binaryArray = binary.split("");
  binaryArray.reverse();
  for (let i = 0; i < binaryArray.length; i++) {
    if (binaryArray[i] === "1") {
      decimal += Math.pow(2, i);
    }
  }
  return decimal;
};

const ogres = convertBinaryToDecimal(ogRows[0].join(""));
const co2res = convertBinaryToDecimal(co2[0].join(""));
console.log("og", ogres);
console.log("co2", co2res);
console.log("total", ogres * co2res);
