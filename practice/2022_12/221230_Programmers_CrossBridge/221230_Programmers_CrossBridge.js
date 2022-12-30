// https://school.programmers.co.kr/learn/courses/30/lessons/64062

function solution(stones, k) {
  let [left, right] = [1, 200000000];

  function canCross(mid) {
    let zeroCount = 0;

    for (let i = 0; i < stones.length; i++) {
      if (stones[i] - mid <= 0) {
        zeroCount++;

        if (zeroCount === k) return false;
      } else zeroCount = 0;
    }

    return true;
  }

  while (left <= right) {
    const mid = ((left + right) / 2) >> 0;
    if (canCross(mid)) left = mid + 1;
    else right = mid - 1;
  }

  return left;
}
