// https://leetcode.com/problems/zigzag-conversion/description/

/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
let convert = function (s, numRows) {
  if (numRows === 1) return s;

  const answer = Array(numRows)
    .fill()
    .map((_) => Array(s).fill(''));

  let i = 0;
  let c = 0;

  while (i < s.length) {
    const mod = c % (numRows - 1);

    if (mod === 0) {
      for (let r = 0; r < numRows; r++) {
        answer[r][c] = s[i++] ?? '';
      }

      c++;
    } else {
      answer[numRows - 1 - mod][c] = s[i++];
      c++;
    }
  }

  return answer.map((a) => a.join('')).join('');
};
