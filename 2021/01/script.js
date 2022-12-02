const fs = require("fs");

const numbers = fs
  .readFileSync("./input.txt", "utf8")
  .toString()
  .split("\n")
  .map(Number);

// given the array of numbers, find how many times an element is greater than the previous element
function countGreaterThanPrevious(numbers) {
  let count = 0;
  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] > numbers[i - 1]) {
      count++;
    }
  }
  return count;
}

console.log("part1", countGreaterThanPrevious(numbers));

// given the array of numbers, convert it in into an array of numbers where each element is a sum of the previous 3 elements
function convertToSlidingSum3(numbers) {
  const slidingSum3 = [];
  for (let i = 2; i < numbers.length; i++) {
    slidingSum3.push(numbers[i - 2] + numbers[i - 1] + numbers[i]);
  }
  return slidingSum3;
}

console.log("part2", countGreaterThanPrevious(convertToSlidingSum3(numbers)));
