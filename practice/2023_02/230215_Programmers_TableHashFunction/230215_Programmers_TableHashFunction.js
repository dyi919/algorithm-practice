// https://school.programmers.co.kr/learn/courses/30/lessons/147354

function solution(data, col, row_begin, row_end) {
  data.sort((a, b) => {
    if (a[col - 1] < b[col - 1]) return -1;
    else if (a[col - 1] === b[col - 1]) return a[0] > b[0] ? -1 : 1;
    else return 1;
  });

  const S = data.map((row, i) =>
    row.reduce((acc, cur) => acc + (cur % (i + 1)), 0)
  );
  return S.slice(row_begin, row_end).reduce(
    (acc, cur) => acc ^ cur,
    S[row_begin - 1]
  );
}
