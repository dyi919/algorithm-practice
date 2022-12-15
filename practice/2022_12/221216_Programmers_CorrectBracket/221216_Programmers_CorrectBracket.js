// https://school.programmers.co.kr/learn/courses/30/lessons/12909

function isEvenLength(s) {
  return s.length % 2 === 0;
}

function isCorrectPair(s) {
  let numOpenBracket = 0;
  const strLength = s.length;

  for (let i = 0; i < strLength; i++) {
    s[i] === "(" ? (numOpenBracket += 1) : (numOpenBracket -= 1);

    if (numOpenBracket < 0) {
      return false;
    }
  }

  if (numOpenBracket > 0) return false;

  return true;
}

function solution(s) {
  return isEvenLength(s) && isCorrectPair(s);
}
