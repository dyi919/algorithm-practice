// https://leetcode.com/problems/delete-columns-to-make-sorted-ii/description/

/**
 * @param {string[]} strs
 * @return {number}
 */
function minDeletionSize(strs) {
  let cols = strs[0].length;
  let n = strs.length;
  const sorted = Array(n).fill(false);
  let count = 0;

  for (let i = 0; i < cols; i++) {
    let isSorted = true;

    for (let k = 0; k < n - 1; k++) {
      if (sorted[k]) continue;

      if (strs[k + 1][i] < strs[k][i]) {
        count++;
        isSorted = false;
        break;
      }
    }

    if (!isSorted) continue;

    for (let k = 0; k < n - 1; k++) {
      sorted[k] ||= strs[k + 1][i] > strs[k][i];
    }
  }

  return count;
}
