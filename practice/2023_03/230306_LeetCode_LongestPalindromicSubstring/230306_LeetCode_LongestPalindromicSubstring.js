// https://leetcode.com/problems/longest-palindromic-substring/description/

/**
 * @param {string} s
 * @return {string}
 */
let longestPalindrome = function (s) {
  let answer = '';

  for (let i = 0; i < s.length; i++) {
    for (let j = s.length; j >= i; j--) {
      if (j - i < answer.length) break;

      const substr = s.slice(i, j);
      if (isPalindrome(substr)) answer = substr;
    }
  }

  return answer;
};

function isPalindrome(s) {
  let [left, right] = [0, s.length - 1];

  while (left < right) {
    if (s[left] !== s[right]) return false;

    left++;
    right--;
  }

  return true;
}
