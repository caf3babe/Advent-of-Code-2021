const fs = require("fs");

function getIncresedValues(numbers) {
  let previous = 0;
  let count = 0;
  numbers.forEach((number) => {
    if (previous == 0) {
      previous = number;
      return;
    }
    if (number > previous) {
      count = count + 1;
    }
    previous = number;
  });
  return count;
}

const fileName = "./day-one-input.txt";

const runDayOneTask = function (error, data) {
  if (error) {
    throw error;
  } else {
    lines = data.split("\n");
    numbers = lines.map(line => parseInt(line));
    console.log(getIncresedValues(numbers));
  }
};

fs.readFile(fileName, "utf8", runDayOneTask);
