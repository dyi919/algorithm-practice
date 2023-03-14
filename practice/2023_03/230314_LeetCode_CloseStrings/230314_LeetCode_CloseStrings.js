// https://leetcode.com/problems/determine-if-two-strings-are-close/

/**
 * @param {string} word1
 * @param {string} word2
 * @return {boolean}
 */
let closeStrings = function (word1, word2) {
  function getCharCount(word1, word2) {
    const charCount = {};

    for (const char of 'abcdefghijklmnopqrstuvwxyz') {
      charCount[char] = [0, 0];
    }

    for (let i = 0; i < word1.length; i++) {
      charCount[word1[i]][0]++;
      charCount[word2[i]][1]++;
    }

    return charCount;
  }

  if (word1.length !== word2.length) return false;

  const charCount = getCharCount(word1, word2);
  const [countStack1, countStack2] = [[], []];

  for (const [charCount1, charCount2] of Object.values(charCount)) {
    if ((charCount1 === 0 || charCount2 === 0) && charCount1 !== charCount2)
      return false;

    countStack1.push(charCount1);
    countStack2.push(charCount2);
  }

  countStack1.sort((a, b) => a - b);
  countStack2.sort((a, b) => a - b);

  for (let i = 0; i < countStack1.length; i++) {
    if (countStack1[i] !== countStack2[i]) return false;
  }

  return true;
};
