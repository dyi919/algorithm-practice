// https://leetcode.com/problems/combinations/description/

/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
let combine = function (n, k) {
  const nums = Array.from({ length: n }, (_, i) => i + 1);
  const result = [];

  function buildComb(cur, remaining) {
    if (cur.length === k) {
      result.push(cur);
      return;
    }
    remaining.forEach((num, i) => {
      buildComb([...cur, num], remaining.slice(i + 1));
    });
  }

  buildComb([], nums);
  return result;
};
