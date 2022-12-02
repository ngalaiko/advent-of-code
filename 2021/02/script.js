const fs = require("fs");

const parseCommand = text => {
  const [command, argument] = text.split(" ");
  return {
    command,
    argument: parseInt(argument)
  };
};

const commands = fs
  .readFileSync("./input.txt", "utf8")
  .toString()
  .split("\n")
  .filter(s => s.length > 0)
  .map(parseCommand);

const upPart1 = ({ x, z }, argument) => {
  return { x, z: z - argument };
};

const downPart1 = ({ x, z }, argument) => {
  return { x, z: z + argument };
};

const forwardPart1 = ({ x, z }, argument) => {
  return { x: x + argument, z };
};

const computerPart1 = {
  up: upPart1,
  down: downPart1,
  forward: forwardPart1
};

const computePart1 = (coordinates, { command, argument }) => {
  return computerPart1[command](coordinates, argument);
};

const start = { x: 0, z: 0, aim: 0 };

const resultPart1 = commands.reduce(computePart1, start);
console.log("part1", resultPart1.x * resultPart1.z);

const up = ({ x, z, aim }, argument) => {
  return { x, z, aim: aim - argument };
};

const down = ({ x, z, aim }, argument) => {
  return { x, z, aim: aim + argument };
};

const forward = ({ x, z, aim }, argument) => {
  return { x: x + argument, z: z + aim * argument, aim };
};

const computer = {
  up,
  down,
  forward
};

const compute = (coordinates, { command, argument }) => {
  return computer[command](coordinates, argument);
};

const result = commands.reduce(compute, start);
console.log("part2", result.x * result.z);
