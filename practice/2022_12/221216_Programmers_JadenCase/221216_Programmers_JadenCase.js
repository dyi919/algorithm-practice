// https://school.programmers.co.kr/learn/courses/30/lessons/12951

function convertToJadenCase(word) {
  const firstLetter = word.slice(0, 1).toUpperCase();
  const restLetters = word.slice(1).toLowerCase();
  const jadenCaseWord = firstLetter + restLetters;

  return jadenCaseWord;
}

function solution(s) {
  let wordArr = [];
  const arr = s.split(" ");

  arr.forEach((word) => (wordArr = [...wordArr, convertToJadenCase(word)]));

  return wordArr.join(" ");
}
