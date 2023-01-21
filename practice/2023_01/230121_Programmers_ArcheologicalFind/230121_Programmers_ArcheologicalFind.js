// https://school.programmers.co.kr/learn/courses/30/lessons/131702

function solution(clockHands) {
  const N = clockHands.length;
  let answer = Infinity;

  for (let k = 0; k < 4 ** N; k++) {
    const _clockHands = clockHands.map((val) => [...val]);
    let rotateCount = 0;
    let dividend = k;

    for (let col = 0; col < N; col++) {
      const count = dividend % 4;

      rotate(_clockHands, 0, col, count);

      rotateCount += count;
      dividend -= count;
      dividend /= 4;
    }

    for (let row = 1; row < N; row++) {
      for (let col = 0; col < N; col++) {
        const count = (4 - _clockHands[row - 1][col]) % 4;

        rotate(_clockHands, row, col, count);

        rotateCount += count;
      }
    }

    if (isSolved(_clockHands)) {
      answer = Math.min(answer, rotateCount);
    }
  }

  return answer;

  function rotate(arr, r, c, cnt) {
    const [dr, dc] = [
      [-1, 0, 0, 0, 1],
      [0, -1, 0, 1, 0],
    ];

    for (let i = 0; i < 5; i++) {
      const [nr, nc] = [r + dr[i], c + dc[i]];

      if (!withinBoundary(nr) || !withinBoundary(nc)) continue;

      arr[nr][nc] += cnt;
      arr[nr][nc] %= 4;
    }
  }

  function withinBoundary(x) {
    return 0 <= x && x < N;
  }

  function isSolved(arr) {
    return arr[N - 1].every((val) => val === 0);
  }
}
