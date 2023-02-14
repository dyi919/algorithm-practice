// https://school.programmers.co.kr/learn/courses/30/lessons/150368

function solution(users, emoticons) {
  const discounts = [10, 20, 30, 40];

  const discountComb = Array(emoticons.length)
    .fill()
    .map((a) => discounts)
    .reduce(
      (acc, cur) => {
        let newAcc = [];
        acc.forEach((arr) => {
          cur.forEach((rate) => {
            newAcc.push([...arr, rate]);
          });
        });
        return newAcc;
      },
      [[]]
    );

  let maxPlusUser = 0;
  let maxRevenue = 0;

  for (const c of discountComb) {
    let revenue = 0;
    let plusUser = 0;

    for (const [minRatio, maxPrice] of users) {
      let totalPrice = 0;
      let isPlusUser = false;

      for (let i = 0; i < emoticons.length; i++) {
        if (c[i] >= minRatio) totalPrice += (emoticons[i] / 100) * (100 - c[i]);
        if (totalPrice >= maxPrice) {
          isPlusUser = true;
          break;
        }
      }

      if (isPlusUser) plusUser++;
      else revenue += totalPrice;
    }

    if (plusUser > maxPlusUser) {
      maxPlusUser = plusUser;
      maxRevenue = revenue;
    } else if (plusUser === maxPlusUser) {
      maxRevenue = Math.max(revenue, maxRevenue);
    }
  }

  return [maxPlusUser, maxRevenue];
}
