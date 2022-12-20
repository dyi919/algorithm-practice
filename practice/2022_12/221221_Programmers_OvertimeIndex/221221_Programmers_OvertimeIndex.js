function sum(arr) {
  return arr.reduce((acc, cur) => acc + cur, 0);
}

function solution(n, works) {
  if (sum(works) <= n) return 0;

  let hourLeft = n;

  let _works = works.sort((a, b) => b - a);

  while (hourLeft > 0) {
    let maxVal = _works[0];
    if (maxVal <= 0) return 0;

    const decrease = Math.min(
      _works.filter((a) => a === maxVal).length,
      hourLeft
    );
    _works = _works.map((a, i) => (a === maxVal && i < decrease ? a - 1 : a));
    hourLeft -= decrease;
  }

  return sum(_works.map((a) => a ** 2));
}
