// https://school.programmers.co.kr/learn/courses/30/lessons/150369

function solution(cap, n, deliveries, pickups) {
  let answer = 0;
  let totalDeliveries = 0;
  let totalPickups = 0;
  deliveries = [0, ...deliveries];
  pickups = [0, ...pickups];

  for (let i = n; i > 0; i--) {
    let count = 0;

    totalDeliveries -= deliveries[i];
    totalPickups -= pickups[i];

    while (totalDeliveries < 0 || totalPickups < 0) {
      totalDeliveries += cap;
      totalPickups += cap;
      count++;
    }

    answer += count * i * 2;
  }

  return answer;
}
