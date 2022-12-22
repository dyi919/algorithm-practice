// https://school.programmers.co.kr/learn/courses/30/lessons/12987

function solution(A, B) {
  const _A = A.sort((a, b) => a - b);
  const _B = B.sort((a, b) => a - b);
  let answer = 0;
  let prevIdx = 0;

  for (let i = 0; i < _B.length; i++) {
    if (_A[prevIdx] < _B[i]) {
      prevIdx++;
      answer++;
    }
  }

  return answer;
}
