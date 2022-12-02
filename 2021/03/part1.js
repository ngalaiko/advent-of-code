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
  .split("\n")
  .filter(s => s.length > 0)
  .map(binaryToArray);

const sumArrayIndices = (a1, a2) => {
  for (let i = 0; i < a1.length; i++) {
    a1[i] += a2[i];
  }
  return a1;
};

const result = rows.slice(1).reduce((acc, current) => {
  return sumArrayIndices(acc, current);
}, rows[0]);

const countGamma = (counts, total) => {
  return counts.map(c => (c > total / 2 ? 1 : 0)).join("");
};

const countEpsilon = (counts, total) => {
  return counts.map(c => (c > total / 2 ? 0 : 1)).join("");
};

const gamma = countGamma(result, rows.length);
const epsilon = countEpsilon(result, rows.length);

console.log("gamma", gamma);
console.log("epsilon", epsilon);
console.log(
  "answer1",
  convertBinaryToDecimal(gamma) * convertBinaryToDecimal(epsilon)
);
