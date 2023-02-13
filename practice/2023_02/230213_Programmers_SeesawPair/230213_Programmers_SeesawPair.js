// https://school.programmers.co.kr/learn/courses/30/lessons/152996

function solution(weights) {
  let answer = 0;
  const weightsCount = Array(2001).fill(0);

  weights.sort((a, b) => a - b);
  weights.forEach((w) => weightsCount[w]++);

  for (const w of weights) {
    answer += --weightsCount[w];
    if (w % 2 === 0) answer += weightsCount[parseInt((w * 3) / 2)];
    answer += weightsCount[w * 2];
    if (w % 3 === 0) answer += weightsCount[parseInt((w * 4) / 3)];
  }

  return answer;
}
