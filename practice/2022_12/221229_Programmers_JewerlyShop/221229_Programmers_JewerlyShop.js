// school.programmers.co.kr/learn/courses/30/lessons/67258

function solution(gems) {
  Map.prototype.add = function (elem) {
    this.set(elem, this.has(elem) ? this.get(elem) + 1 : 1);
  };

  Map.prototype.remove = function (elem) {
    const val = this.get(elem);
    if (val === 1) this.delete(elem);
    else this.set(elem, val - 1);
  };

  let answer = [];
  let totalGems = new Set(gems).size;
  let currentGems = new Map([[gems[0], 1]]);
  let shortestInterval = gems.length;
  let lo = 0;
  let hi = 0;

  while (hi < gems.length && lo <= hi) {
    if (currentGems.size === totalGems) {
      if (hi - lo < shortestInterval) {
        shortestInterval = hi - lo;
        answer = [lo + 1, hi + 1];
      }

      currentGems.remove(gems[lo]);
      lo++;
    } else {
      hi++;
      currentGems.add(gems[hi]);
    }
  }

  return answer;
}
