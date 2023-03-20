// https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/submissions/918756709/

/**
 * @param {string} s
 * @param {string} locked
 * @return {boolean}
 */
function canBeValid(s, locked) {
  function validate(s, locked, op) {
    let balance = 0;
    let wild = 0;

    for (let i = 0; i < s.length; i++) {
      if (locked[i] === '1') {
        if (s[i] === op) balance++;
        else balance--;
      } else {
        wild++;
      }
      if (balance + wild < 0) return false;
    }

    return balance <= wild;
  }

  return (
    s.length % 2 === 0 &&
    validate(s, locked, '(') &&
    validate(Array.from(s).reverse(), Array.from(locked).reverse(), ')')
  );
}
