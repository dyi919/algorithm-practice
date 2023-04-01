// https://school.programmers.co.kr/learn/courses/30/lessons/172928

const COMMANDS = {
  N: [-1, 0],
  S: [1, 0],
  W: [0, -1],
  E: [0, 1],
};

function solution(park, routes) {
  function isValidPosition(pos, R, C, park) {
    const [r, c] = pos;

    return r >= 0 && r < R && c >= 0 && c < C && park[r][c] !== 'X';
  }

  let pos = [-1, -1];
  const [R, C] = [park.length, park[0].length];

  for (let i = 0; i < R; i++) {
    for (let j = 0; j < C; j++) {
      if (park[i][j] === 'S') {
        pos = [i, j];
        break;
      }
    }
  }

  for (const route of routes) {
    const [op, n] = route.split(' ');

    let tempPos = pos;
    let isValidMove = true;

    for (let i = 0; i < n; i++) {
      let newPos = [tempPos[0] + COMMANDS[op][0], tempPos[1] + COMMANDS[op][1]];
      tempPos = newPos;

      if (!isValidPosition(newPos, R, C, park)) {
        isValidMove = false;
        break;
      }
    }

    if (isValidMove) pos = tempPos;
  }

  return pos;
}
