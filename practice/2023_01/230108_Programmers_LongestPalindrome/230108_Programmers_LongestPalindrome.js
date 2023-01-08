// https://school.programmers.co.kr/learn/courses/30/lessons/12904

function solution(s) {
  let answer = 1;

  const L = s.length;
  const cache = Array(L)
    .fill()
    .map((_) => Array(L).fill(false));

  for (let i = 0; i < L; i++) {
    cache[i][i] = true;
  }

  for (let i = 0; i < L - 1; i++) {
    if (s[i] === s[i + 1]) {
      cache[i][i + 1] = true;
      answer = 2;
    }
  }

  for (let len = 3; len <= L; len++) {
    for (let start = 0; start <= L - len; start++) {
      const end = start + len - 1;

      if (s[start] === s[end] && cache[start + 1][end - 1]) {
        cache[start][end] = true;
        answer = len;
      }
    }
  }

  return answer;
}
