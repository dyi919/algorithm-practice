// https://leetcode.com/problems/sentence-similarity-iii/description/

/**
 * @param {string} sentence1
 * @param {string} sentence2
 * @return {boolean}
 */
function areSentencesSimilar(sentence1, sentence2) {
  function check(a1, a2) {
    if (a2.length === 1) {
      return a1[0] === a2[0] || a1[a1.length - 1] === a2[0] ? true : false;
    }

    let [index1, index2] = [0, 0];

    while (
      index1 < a1.length &&
      index2 < a2.length &&
      a1[index1] === a2[index2]
    ) {
      index1++;
      index2++;
    }

    if (index2 === a2.length) return true;

    while (index1 < a1.length && a1[index1] !== a2[index2]) {
      index1++;
    }

    while (
      index1 < a1.length &&
      index2 < a2.length &&
      a1[index1] === a2[index2]
    ) {
      index1++;
      index2++;
    }

    return index1 === a1.length && index2 === a2.length ? true : false;
  }

  if (sentence2.length > sentence1.length) {
    [sentence1, sentence2] = [sentence2, sentence1];
  }

  const [a1, a2] = [sentence1.split(' '), sentence2.split(' ')];

  return check(a1, a2) || check(a1.reverse(), a2.reverse());
}
