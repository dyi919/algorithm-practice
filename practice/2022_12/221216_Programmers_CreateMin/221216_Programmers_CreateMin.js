// https://school.programmers.co.kr/learn/courses/30/lessons/12941

function solution(A, B) {
  const _A = [...A];
  const _B = [...B];
  let sum = 0;

  _A.sort((a, b) => a - b);
  _B.sort((a, b) => b - a);

  const arrLength = _A.length;

  for (let i = 0; i < arrLength; i++) {
    sum += _A[i] * _B[i];
  }

  return sum;
}
