// https://school.programmers.co.kr/learn/courses/30/lessons/72412

function solution(info, query) {
  let answer = [];

  const conditionIndex = {
    cpp: 0,
    java: 1,
    python: 2,
    backend: 0,
    frontend: 1,
    junior: 0,
    senior: 1,
    chicken: 0,
    pizza: 1,
  };
  const conditionMultiplier = [8, 4, 2, 1];
  const options = [3, 2, 2, 2];

  const range = Array(24)
    .fill()
    .map(() => Array(2).fill(-1));

  const sortedArrInfo = info.map((i) => i.split(" ")).sort(sortFn);
  const testScores = sortedArrInfo.map((a) => Number(a[4]));

  let prevRangeIdx = getRangeIndex(sortedArrInfo[0]);
  range[prevRangeIdx][0] = 0;
  range[prevRangeIdx][1] = 1;

  for (let i = 1; i < sortedArrInfo.length; i++) {
    const rangeIdx = getRangeIndex(sortedArrInfo[i]);
    if (prevRangeIdx !== rangeIdx) {
      range[rangeIdx][0] = i;
      range[rangeIdx][1] = i + 1;
      prevRangeIdx = rangeIdx;
    } else range[prevRangeIdx][1]++;
  }

  for (const q of query) {
    let checkIdx = Array(24).fill(true);
    const parsedQuery = parseQuery(q);

    parsedQuery.slice(0, 4).forEach((condition, i) => {
      if (condition === "-") return;
      for (let idx = 0; idx < 24; idx++) {
        const comp =
          Math.floor(idx / conditionMultiplier[i]) % options[i] ===
          conditionIndex[condition];
        if (!comp) checkIdx[idx] = false;
      }
    });

    let count = 0;

    for (let i = 0; i < 24; i++) {
      if (!checkIdx[i]) continue;

      const [start, end] = range[i];
      if (end === -1) continue;
      count += end - bisectLeft(testScores, Number(parsedQuery[4]), start, end);
    }

    answer.push(count);
  }

  return answer;

  function sortFn(a, b) {
    const lastIndex = a.length - 1;

    for (let i = 0; i < lastIndex; i++) {
      if (a[i] === b[i]) continue;

      return a[i].localeCompare(b[i]);
    }

    return a[lastIndex] - b[lastIndex];
  }

  function getRangeIndex(info) {
    return info
      .slice(0, 4)
      .reduce(
        (acc, cur, i) => acc + conditionIndex[cur] * conditionMultiplier[i],
        0
      );
  }

  function parseQuery(query) {
    const queryList = query.split(" and ");
    const [language, position, experience, foodTest] = queryList;
    const [food, test] = foodTest.split(" ");

    return [language, position, experience, food, test];
  }

  function bisectLeft(arr, value, lo, hi) {
    while (lo < hi) {
      const mid = (lo + hi) >> 1;
      if (arr[mid] < value) {
        lo = mid + 1;
      } else {
        hi = mid;
      }
    }
    return lo;
  }
}
