const signals = {
  1: ["c", "f"],

  7: ["a", "c", "f"],

  4: ["b", "c", "d", "f"],

  2: ["a", "c", "d", "e", "g"],
  3: ["a", "c", "d", "f", "g"],
  5: ["a", "b", "d", "f", "g"],

  0: ["a", "b", "c", "e", "f", "g"],
  6: ["a", "b", "d", "e", "f", "g"],
  9: ["a", "b", "c", "d", "f", "g"],

  8: ["a", "b", "c", "d", "e", "f", "g"]
};

const part2 = input => {
  const lines = input.split("\n").filter(line => line.length > 0);
  return lines
    .map(line => {
      const [signalsInput, digitsInput] = line.split("|");
      const digits = digitsInput.split(" ").filter(digit => digit.length > 0);

      const aliases = {};

      const twos = digits.filter(digit => digit.length === 2);
      twos.forEach(digit => {
        for (let i = 0; i < digit.length; i++) {
          const char = digit.charAt(i);
          aliases[char] = "c";
          aliases[char] = "f";
        }
      });
      const sevens = digits.filter(digit => digit.length === 3);
      sevens.forEach(digit => {
        for (let i = 0; i < digit.length; i++) {
          const char = digit.charAt(i);
          if (!aliases[char]) {
            signals[4].forEach(c => (aliases[char] = c));
          }
        }
      });
      const fours = digits.filter(digit => digit.length === 4);
      fours.forEach(digit => {
        for (let i = 0; i < digit.length; i++) {
          const char = digit.charAt(i);
          if (!aliases[char]) {
            signals[4].forEach(c => (aliases[char] = c));
          }
        }
      });
      const eights = digits.filter(digit => digit.length === 6);
      eights.forEach(digit => {
        for (let i = 0; i < digit.length; i++) {
          const char = digit.charAt(i);
          if (!aliases[char]) {
            signals[8].forEach(c => (aliases[char] = c));
          }
        }
      });

      const rest = digits.filter(digit => {
        const length = digit.length;
        if (signals[1].length === length) return false;
        if (signals[4].length === length) return false;
        if (signals[7].length === length) return false;
        if (signals[8].length === length) return false;
        return true;
      });
      console.log(rest, aliases);

      return 0;
    })
    .reduce((a, b) => a + b);
};

const part1 = input => {
  const lines = input.split("\n").filter(line => line.length > 0);
  return lines
    .map(line => {
      const [signalsInput, digitsInput] = line.split("|");
      const digits = digitsInput.split(" ").filter(digit => digit.length > 0);

      const isLengthValid = digit => {
        const length = digit.length;
        if (signals[1].length === length) return true;
        if (signals[4].length === length) return true;
        if (signals[7].length === length) return true;
        if (signals[8].length === length) return true;
        return false;
      };
      return digits.filter(isLengthValid).length;
    })
    .reduce((a, b) => a + b);
};

const fs = require("fs");

["./test.txt", "./input.txt"]
  .map(path => fs.readFileSync(path, "utf8").toString())
  .map(part1)
  .forEach(r => console.log("part1", r));

["./test.txt", "./input.txt"]
  .map(path => fs.readFileSync(path, "utf8").toString())
  .map(part2)
  .forEach(r => console.log("part2", r));
