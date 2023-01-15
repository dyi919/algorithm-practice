// https://school.programmers.co.kr/learn/courses/30/lessons/131703

function flip(arr) {
  return arr.map((a) => (a === 0 ? 1 : 0));
}

function solution(beginning, target) {
  let answer = Infinity;

  const _beginning = [...beginning];
  const row = _beginning.length;
  const col = _beginning[0].length;

  for (let b = 0; b < 2 ** row; b++) {
    const bitmask = b.toString(2).padStart(row, '0');
    const rowFlipped = _beginning.map((row, i) =>
      bitmask[i] === '1' ? flip(row) : row
    );

    answer = Math.min(answer, getCount(rowFlipped, bitmask));
  }

  return answer === Infinity ? -1 : answer;

  function getCount(arr, bitmask) {
    let count = bitmask
      .split('')
      .reduce((acc, cur) => (cur === '1' ? acc + Number(cur) : acc), 0);

    for (let i = 0; i < col; i++) {
      if (count > answer) return Infinity;

      let match = 0;

      for (let j = 0; j < row; j++) {
        if (arr[j][i] === target[j][i]) match++;
      }

      if (match === row) continue;
      if (match === 0) count++;
      else return Infinity;
    }

    return count;
  }
}
