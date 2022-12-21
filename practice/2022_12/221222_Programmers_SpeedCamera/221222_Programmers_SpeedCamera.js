// https://school.programmers.co.kr/learn/courses/30/lessons/42884

function solution(routes) {
  const _routes = routes.sort((a, b) =>
    a[1] !== b[1] ? a[1] - b[1] : a[0] - b[0]
  );
  let answer = 1;
  let prev = _routes[0][1];

  for (let i = 1; i < _routes.length; i++) {
    if (prev < _routes[i][0]) {
      answer++;
      prev = _routes[i][1];
    } else if (prev > _routes[i][1]) {
      prev = _routes[i][1];
    }
  }

  return answer;
}
