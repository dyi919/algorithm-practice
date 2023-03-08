// https://leetcode.com/problems/reverse-integer/description/

/**
 * @param {number} x
 * @return {number}
 */

let reverse = function (x) {
  const MAX_ARR = [2, 1, 4, 7, 4, 8, 3, 6, 4, x < 0 ? 8 : 7];

  let isNegative;
  let digits = [];

  if (x < 0) {
    isNegative = true;
    x = -x;
  }

  while (x > 0) {
    const [quotient, remainder] = [Math.floor(x / 10), x % 10];
    digits = [...digits, remainder];
    x = quotient;
  }

  if (digits.length <= 10) {
    if (digits.length === 10) {
      for (let i = 0; i < 10; i++) {
        if (MAX_ARR[i] < digits[i]) return 0;
        else if (MAX_ARR[i] > digits[i]) break;
      }
    }

    const reversedNum = Number(digits.map((num) => String(num)).join(''));
    return isNegative ? -reversedNum : reversedNum;
  } else {
    return 0;
  }
};
