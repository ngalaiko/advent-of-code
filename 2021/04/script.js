const fs = require("fs");

const input = fs.readFileSync("./input.txt", "utf8").toString();

const testInput = fs.readFileSync("./test.txt", "utf8").toString();

const rows = input.split("\n");

const numbers = rows[0].split(",").map(Number);

const parseBoard = rows => {
  return rows.map(row =>
    row
      .trim()
      .replace(/\s\s+/g, " ")
      .split(" ")
      .map(Number)
      .map(v => {
        return { marked: false, value: v };
      })
  );
};

const boards = [];
for (let i = 2; i < rows.length; i++) {
  const board = parseBoard(rows.slice(i, i + 5));
  boards.push(board);
  i += 5;
}

const mark = (board, number) =>
  board.forEach(row => {
    row.forEach(cell => {
      if (cell.value === number) {
        cell.marked = true;
      }
    });
  });

const isWinning = board => {
  const markedByRows = [0, 0, 0, 0, 0];
  const markedByColumns = [0, 0, 0, 0, 0];
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[i].length; j++) {
      if (board[i][j].marked) {
        markedByRows[i]++;
        if (markedByRows[i] === 5) {
          return true;
        }
        markedByColumns[j]++;
        if (markedByColumns[j] === 5) {
          return true;
        }
      }
    }
  }
};

const score = board => {
  let score = 0;
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[i].length; j++) {
      if (!board[i][j].marked) {
        score += board[i][j].value;
      }
    }
  }
  return score;
};

const winningBoards = {};

numbers.forEach(number => {
  boards.forEach((board, i) => {
    mark(board, number);
    if (!winningBoards[i] && isWinning(board)) {
      winningBoards[i] = true;
      const s = score(board);
      console.log(
        `${number} is winning in board ${i} with score ${s}, result ${s *
          number}`
      );
    }
  });
});
