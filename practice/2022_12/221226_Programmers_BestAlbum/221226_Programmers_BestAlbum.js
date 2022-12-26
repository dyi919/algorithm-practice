// https://school.programmers.co.kr/learn/courses/30/lessons/42579

function solution(genres, plays) {
  let answer = [];
  let countByGenre = {};

  genres.forEach((g, i) => {
    if (countByGenre.hasOwnProperty(g)) {
      countByGenre[g][0] += plays[i];
      countByGenre[g] = [...countByGenre[g], [plays[i], i]];
    } else {
      countByGenre[g] = [plays[i], [plays[i], i]];
    }
  });

  let countByGenreArray = Object.entries(countByGenre).sort(
    (a, b) => b[1][0] - a[1][0]
  );

  countByGenreArray.forEach((a) => {
    const topTwo = a[1]
      .slice(1)
      .sort((a, b) => (a[0] === b[0] ? a[1] - b[1] : b[0] - a[0]))
      .slice(0, 2);
    topTwo.forEach((a) => {
      answer = [...answer, a[1]];
    });
  });

  return answer;
}
