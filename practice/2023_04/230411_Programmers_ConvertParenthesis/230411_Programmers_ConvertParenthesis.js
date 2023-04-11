// https://school.programmers.co.kr/learn/courses/30/lessons/60058

function isBalanced(p) {
  let [openCount, closeCount] = [0, 0];

  Array.from(p).forEach((c) => {
    if (c === '(') openCount++;
    else closeCount++;
  });

  return openCount === closeCount;
}

function isCorrect(p) {
  let openCount = 0;

  for (let i = 0; i < p.length; i++) {
    if (p[i] === '(') openCount++;
    else if (openCount > 0) openCount--;
    else return false;
  }

  return true;
}

function reverseParenthesis(p) {
  return Array.from(p)
    .map((c) => (c === '(' ? ')' : '('))
    .join('');
}

function solution(p) {
  if (p === '') return p;

  for (let i = 2; i <= p.length; i += 2) {
    const [u, v] = [p.slice(0, i), p.slice(i)];

    if (!isBalanced(u)) continue;

    if (isCorrect(u)) {
      return u + solution(v);
    } else {
      const strippedU = u.slice(1, u.length - 1);
      return `(${solution(v)})${reverseParenthesis(strippedU)}`;
    }
  }
}
