// https://leetcode.com/problems/equal-row-and-column-pairs/submissions/913734134/

/**
 * @param {number[][]} grid
 * @return {number}
 */
let equalPairs = function (grid) {
  const rows = grid.map((row) => row.join());
  const cols = grid[0].map((col, i) => grid.map((row) => row[i]).join());

  let count = 0;

  for (const row of rows) {
    for (const col of cols) {
      if (row === col) count++;
    }
  }

  return count;
};
