// https://school.programmers.co.kr/learn/courses/30/lessons/138475

function solution(e, starts) {
  const countCache = Array(e + 1).fill(0);
  const ansCache = Array(e + 1).fill(0);

  for (let i = 1; i <= e; i++) {
    for (let j = 1; j <= Math.floor(e / i); j++) {
      countCache[i * j]++;
    }
  }

  let maxVal = 0;
  let maxIdx = 0;

  for (let i = e; i > 0; i--) {
    if (countCache[i] >= maxVal) {
      maxVal = countCache[i];
      maxIdx = i;
    }
    ansCache[i] = maxIdx;
  }

  return starts.map((s) => ansCache[s]);
}
