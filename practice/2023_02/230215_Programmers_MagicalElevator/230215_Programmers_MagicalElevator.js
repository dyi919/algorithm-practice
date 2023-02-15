// https://school.programmers.co.kr/learn/courses/30/lessons/148653

function solution(storey) {
  let result = 0;
  const digits = String(storey)
    .split("")
    .map((a) => Number(a));

  for (let i = digits.length - 1; i >= 0; i--) {
    if (digits[i] > 5) {
      result += 10 - digits[i];
      digits[i - 1]++;

      if (i === 0) {
        result++;
      }
    } else if (digits[i] === 5 && i > 0 && digits[i - 1] >= 5) {
      result += 5;
      digits[i - 1]++;
    } else {
      result += digits[i];
    }
  }

  return result;
}
