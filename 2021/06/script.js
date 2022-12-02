const fs = require("fs");

const input = fs.readFileSync("./input.txt", "utf8").toString();

const testInput = fs.readFileSync("./test.txt", "utf8").toString();

const tick = age => {
  if (age === 0) {
    return [6, 8];
  }
  return [age - 1];
};

const cache = {};

const fishCountOnDay = (fishAge, dayNumber) => {
  const key = `age:${fishAge}, day: ${dayNumber}`;
  if (cache[key]) {
    return cache[key];
  }

  dayNumber -= fishAge;
  let count = 1;
  for (let i = 0; i < dayNumber; i += 7) {
    count += fishCountOnDay(9, dayNumber - i);
  }
  cache[key] = count;
  return count;
};

const solve = input => {
  return input
    .split(",")
    .map(age => Number(age))
    .map(age => fishCountOnDay(age, 256))
    .reduce((a, b) => a + b);
};

[testInput, input].map(solve).forEach(r => console.log(r));
