// https://leetcode.com/problems/minimum-path-sum/description/

/**
 * @param {number[][]} grid
 * @return {number}
 */
let minPathSum = function (grid) {
  const [N, M] = [grid.length, grid[0].length];
  const cache = Array(N)
    .fill()
    .map((_) => Array(M).fill(0));
  cache[0][0] = grid[0][0];

  for (let i = 1; i < M; i++) {
    cache[0][i] = cache[0][i - 1] + grid[0][i];
  }

  for (let i = 1; i < N; i++) {
    cache[i][0] = cache[i - 1][0] + grid[i][0];
  }

  for (let i = 1; i < N; i++) {
    for (let j = 1; j < M; j++) {
      cache[i][j] = Math.min(cache[i - 1][j], cache[i][j - 1]) + grid[i][j];
    }
  }

  return cache[N - 1][M - 1];
};
