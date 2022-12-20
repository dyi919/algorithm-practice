// https://school.programmers.co.kr/learn/courses/30/lessons/12938?language=javascript

function solution(n, s) {
  if (s < n) return [-1];

  const val = Math.floor(s / n);
  const remainder = s % n;
  const answer = [
    ...new Array(n - remainder).fill(val),
    ...new Array(remainder).fill(val + 1),
  ];

  return answer;
}
