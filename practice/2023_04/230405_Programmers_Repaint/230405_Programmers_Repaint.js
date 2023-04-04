// https://school.programmers.co.kr/learn/courses/30/lessons/161989

function solution(n, m, section) {
  let answer = 0;
  let prevPos = 0;

  for (let i = 0; i < section.length; i++) {
    if (prevPos >= section[i]) continue;

    prevPos = section[i] + m - 1;
    answer++;
  }

  return answer;
}
