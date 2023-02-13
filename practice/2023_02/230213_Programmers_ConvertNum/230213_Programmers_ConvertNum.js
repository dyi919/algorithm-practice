// https://school.programmers.co.kr/learn/courses/30/lessons/154538

function solution(x, y, n) {
  const cache = Array(y + 1).fill(-1);
  const queue = [x];

  cache[x] = 0;

  while (queue.length > 0) {
    const curVal = queue.shift();

    for (const nextVal of [curVal + n, curVal * 2, curVal * 3]) {
      if (nextVal === y) return cache[curVal] + 1;

      if (nextVal > y) continue;

      if (cache[nextVal] === -1) {
        cache[nextVal] = cache[curVal] + 1;
        queue.push(nextVal);
      }
    }
  }

  return cache[y];
}
