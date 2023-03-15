// https://leetcode.com/problems/find-triangular-sum-of-an-array/description/

/**
 * @param {number[]} nums
 * @return {number}
 */
let triangularSum = function (nums) {
  let newNums = [...nums];

  while (newNums.length > 1) {
    let tempNums = [];

    for (let i = 0; i < newNums.length - 1; i++) {
      tempNums.push((newNums[i] + newNums[i + 1]) % 10);
    }

    newNums = [...tempNums];
  }

  return newNums[0];
};
