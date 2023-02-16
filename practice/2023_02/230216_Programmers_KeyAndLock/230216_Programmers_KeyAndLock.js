// https://school.programmers.co.kr/learn/courses/30/lessons/60059?language=javascript

let M;
let N;

function rotate(key) {
  const rotatedKey = Array(M)
    .fill()
    .map(() => Array(M).fill(0));

  for (let i = 0; i < M; i++) {
    for (let j = 0; j < M; j++) {
      if (key[i][j] === 1) {
        rotatedKey[j][M - i - 1] = 1;
      }
    }
  }

  return rotatedKey;
}

function move(key, x, y) {
  let movedKey;

  if (x < 0) {
    movedKey = key.map((row) => [...row, ...Array(-x).fill(0)].slice(-M));
  } else if (x > 0) {
    movedKey = key.map((row) => [...Array(x).fill(0), ...row].slice(0, M));
  } else {
    movedKey = key.map((row) => [...row]);
  }

  if (y < 0) {
    movedKey = [
      ...movedKey,
      ...Array(-y)
        .fill()
        .map(() => Array(M).fill(0)),
    ].slice(-M);
  } else if (y > 0) {
    movedKey = [
      ...Array(y)
        .fill()
        .map(() => Array(M).fill(0)),
      ...movedKey,
    ].slice(0, M);
  } else {
    movedKey = [...movedKey];
  }

  return movedKey;
}

function fit(key, lock) {
  const diff = N - M;

  for (let rDiff = 0; rDiff <= diff; rDiff++) {
    for (let cDiff = 0; cDiff <= diff; cDiff++) {
      const board = lock.map((row) => [...row]);

      for (let i = rDiff; i < M + rDiff; i++) {
        for (let j = cDiff; j < M + cDiff; j++) {
          board[i][j] += key[i - rDiff][j - cDiff];
        }
      }

      let isFit = board.every((row) => row.every((x) => x === 1));

      if (isFit) return true;
    }
  }

  return false;
}

function solution(key, lock) {
  let answer = true;

  M = key.length;
  N = lock.length;

  let currentKey = key;

  for (let k = 0; k < 4; k++) {
    for (let i = -M + 1; i < M; i++) {
      for (let j = -M + 1; j < M; j++) {
        let movedKey = move(currentKey, i, j);

        if (fit(movedKey, lock)) return true;
      }
    }

    currentKey = rotate(currentKey);
  }

  return false;
}
