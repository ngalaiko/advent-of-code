const median = numbers => {
  const mid = Math.floor(numbers.length / 2);
  const nums = numbers.sort((a, b) => a - b);
  return numbers.length % 2 !== 0 ? nums[mid] : (nums[mid - 1] + nums[mid]) / 2;
};

const part1 = input => {
  const positions = input.split(",").map(Number);
  const medianPosition = median(positions);
  return positions
    .map(position => Math.abs(position - medianPosition))
    .reduce((a, b) => a + b);
};

const fuelCost = distance => (distance * distance + distance) / 2;

const average = numbers => {
  const sum = numbers.reduce((a, b) => a + b, 0);
  return sum / numbers.length;
};

const part2 = input => {
  const positions = input.split(",").map(Number);
  // const averageCeil = Math.ceil(average(positions));
  const averageFloor = Math.floor(average(positions));
  return positions
    .map(position => fuelCost(Math.abs(position - averageFloor)))
    .reduce((a, b) => a + b);
};

const fs = require("fs");

["./test.txt", "./input.txt"]
  .map(path => fs.readFileSync(path, "utf8").toString())
  .map(part1)
  .forEach(r => console.log(r));

["./test.txt", "./input.txt"]
  .map(path => fs.readFileSync(path, "utf8").toString())
  .map(part2)
  .forEach(r => console.log(r));
