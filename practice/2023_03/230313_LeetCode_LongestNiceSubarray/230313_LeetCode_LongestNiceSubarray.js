// https://leetcode.com/problems/longest-nice-subarray/submissions/914337958/

/**
 * @param {number[]} nums
 * @return {number}
 */
let longestNiceSubarray = function (nums) {
  let bits = 0;
  let maxLength = 1;
  let [left, right] = [0, 0];

  while (right < nums.length) {
    if ((bits & nums[right]) !== 0) {
      bits ^= nums[left++];
    } else {
      bits |= nums[right++];
      maxLength = Math.max(maxLength, right - left);
    }
  }

  return maxLength;
};
