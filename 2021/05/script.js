const fs = require("fs");

const input = fs.readFileSync("./input.txt", "utf8").toString();

const testInput = fs.readFileSync("./test.txt", "utf8").toString();

const run = input => {
  const rows = input.split("\n").filter(r => r.length > 0);

  const lines = rows.map(row => {
    const [start, end] = row.split(" -> ");
    return [start.split(",").map(Number), end.split(",").map(Number)];
  });

  // given coordinates of two dots, find all the coordinates between them
  // including the diagonals
  const covered = ([x1, y1], [x2, y2]) => {
    const x = x1 < x2 ? x1 : x2;
    const y = y1 < y2 ? y1 : y2;
    const w = Math.abs(x1 - x2);
    const h = Math.abs(y1 - y2);
    const result = [];
    for (let i = 0; i <= w; i++) {
      for (let j = 0; j <= h; j++) {
        result.push([x + i, y + j]);
      }
    }
    return result;
  };

  const diagonal = ([x1, y1], [x2, y2]) => {
    const directionX = x1 < x2 ? 1 : -1;
    const directionY = y1 < y2 ? 1 : -1;
    const result = [];
    for (let i = 0; i <= Math.abs(x1 - x2); i++) {
      result.push([x1 + i * directionX, y1 + i * directionY]);
    }
    return result;
  };

  const field = lines
    .flatMap(([[x1, y1], [x2, y2]]) => {
      if (x1 !== x2 && y1 !== y2) return diagonal([x1, y1], [x2, y2]);
      return covered([x1, y1], [x2, y2]);
    })
    .reduce((field, [x, y]) => {
      if (field[x] === undefined) field[x] = {};
      if (field[x][y] === undefined) field[x][y] = 0;
      field[x][y]++;
      return field;
    }, {});

  let count = 0;
  for (let x in field) {
    for (let y in field[x]) {
      if (field[x][y] >= 2) {
        count++;
      }
    }
  }

  return count;
};

[input, testInput].map(run).forEach(r => console.log(r));
