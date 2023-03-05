/**
 * @param {string} s
 * @return {number}
 */
let lengthOfLongestSubstring = function (s) {
  let [left, right] = [0, 0];
  let map = new Map();
  let maxLen = 0;

  for (let i = 0; i < s.length; i++) {
    const prev = map.get(s[i]);

    if (prev !== undefined && prev >= left) {
      left = prev + 1;
    }

    map.set(s[i], i);

    right++;
    maxLen = maxLen < right - left ? right - left : maxLen;
  }

  return maxLen;
};
