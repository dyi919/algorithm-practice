// https://school.programmers.co.kr/learn/courses/30/lessons/17685

function getCount(a, b) {
  let i = 0;
  while (i < a.length && a[i] === b[i]) i++;
  return i + 1;
}

function solution(words) {
  const sortedWords = words.sort();
  const N = sortedWords.length;
  let answer = 0;
  let prev = 0;

  for (let i = 0; i < N - 1; i++) {
    let count = getCount(sortedWords[i], sortedWords[i + 1]);

    answer += Math.max(prev, Math.min(count, sortedWords[i].length));
    prev = count;
  }
  answer += prev;
  return answer;
}
