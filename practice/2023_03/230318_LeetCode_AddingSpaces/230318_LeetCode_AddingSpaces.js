//https://leetcode.com/problems/adding-spaces-to-a-string/description/

/**
 * @param {string} s
 * @param {number[]} spaces
 * @return {string}
 */
function addSpaces(s, spaces) {
  let answer = s.slice(0, spaces[0]);
  let prev = spaces[0];

  for (const space of spaces.slice(1)) {
    answer += ' ' + s.slice(prev, space);
    prev = space;
  }

  answer += ' ' + s.slice(prev);

  return answer;
}
