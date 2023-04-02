// https://school.programmers.co.kr/learn/courses/30/lessons/161990

function solution(wallpaper) {
  const [R, C] = [wallpaper.length, wallpaper[0].length];
  let [lux, luy, rdx, rdy] = [R - 1, C - 1, 0, 0];

  for (let i = 0; i < R; i++) {
    for (let j = 0; j < C; j++) {
      if (wallpaper[i][j] === '.') continue;

      const [x, y] = [i, j];

      if (lux > x) lux = x;
      if (rdx < x + 1) rdx = x + 1;

      if (luy > y) luy = y;
      if (rdy < y + 1) rdy = y + 1;
    }
  }

  return [lux, luy, rdx, rdy];
}
