// https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/description/

/**
 * @param {number} n
 * @return {number}
 */
let twoEggDrop = function (n) {
  let pos = 1;
  let move = 1;

  while (pos < n) {
    move++;
    pos += move;
  }

  return move;
};
