#!/usr/bin/node

function bubbleSort (arr) {
  let i;
  let j;
  let temp;

  for (i = 0; i < arr.length; i++) {
    for (j = 0; j < (arr.length - i - 1); j++) {
      if (arr[j] > arr[j + 1]) {
        temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
  console.log(arr[arr.length - 2]);
}

const argv = process.argv;
const myArr = argv.filter(function (x) { return (!isNaN(x)); });
let i = 0;

if (argv.length <= 3) {
  console.log(0);
} else {
  for (i = 0; i < myArr.length; i++) {
    myArr[i] = parseInt(myArr[i]);
  }
  bubbleSort(myArr);
}
