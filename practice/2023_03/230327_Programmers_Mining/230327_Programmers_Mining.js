// https://school.programmers.co.kr/learn/courses/30/lessons/172927

const indexDict = {
  diamond: 0,
  iron: 1,
  stone: 2,
};

function solution(picks, minerals) {
  let answer = 0;
  let _picks = [...picks];
  let _minerals = [...minerals];
  const totalPicksNum = _picks.reduce((acc, cur) => acc + cur, 0);

  if (Math.ceil(minerals.length / 5) > totalPicksNum) {
    _minerals = minerals.slice(0, totalPicksNum * 5);
  }

  const separatedMinerals = [];
  for (let i = 0; i < _minerals.length; i += 5) {
    separatedMinerals.push(
      _minerals.slice(i, Math.min(i + 5, _minerals.length))
    );
  }

  const mineralCounts = separatedMinerals.reduce((acc, minerals) => {
    const count = [0, 0, 0];

    for (const mineral of minerals) {
      count[indexDict[mineral]]++;
    }

    return [...acc, count];
  }, []);

  mineralCounts.sort((a, b) => {
    let mul = 25;
    let [weightA, weightB] = [0, 0];

    for (let i = 0; i < 3; i++) {
      weightA += a[i] * mul;
      weightB += b[i] * mul;
      mul /= 5;
    }

    return weightB - weightA;
  });

  mineralCounts.forEach((count) => {
    let i = 0;

    while (_picks[i] === 0) i++;

    if (i === 0) {
      answer += count[0] + count[1] + count[2];
    } else if (i === 1) {
      answer += count[0] * 5 + count[1] + count[2];
    } else {
      answer += count[0] * 25 + count[1] * 5 + count[2];
    }

    _picks[i]--;
  });

  return answer;
}
