// https://school.programmers.co.kr/learn/courses/30/lessons/176963

function solution(name, yearning, photo) {
  let yearningDict = {};

  for (let i = 0; i < name.length; i++) {
    yearningDict[name[i]] = yearning[i];
  }

  return photo.map((people) =>
    people.reduce((acc, person) => acc + (yearningDict[person] ?? 0), 0)
  );
}
