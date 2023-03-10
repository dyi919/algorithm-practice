// https://leetcode.com/problems/non-decreasing-array/description/

/**
 * @param {number[]} nums
 * @return {boolean}
 */
let checkPossibility = function (nums) {
  let count = 1;
  let i = 1;

  while (i < nums.length) {
    if (nums[i - 1] > nums[i]) {
      if (count > 0) {
        count--;
        if (i > 1 && nums[i - 2] > nums[i]) nums[i] = nums[i - 1];
      } else return false;
    }
    i++;
  }

  return true;
};
