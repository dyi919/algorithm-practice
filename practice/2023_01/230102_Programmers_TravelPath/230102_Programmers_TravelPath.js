// https://school.programmers.co.kr/learn/courses/30/lessons/43164

function solution(tickets) {
  const cities = tickets.length + 1;
  let flights = new Map();

  function dfs(arr, flights, count) {
    const cur = arr[arr.length - 1];

    if (!flights.has(cur)) return arr;

    const destinations = flights.get(cur);

    for (let i = 0; i < destinations.length; i++) {
      const newFlights = new Map([...flights]);
      newFlights.set(cur, [
        ...destinations.slice(0, i),
        ...destinations.slice(i + 1),
      ]);

      const result = dfs([...arr, destinations[i]], newFlights, count + 1);
      if (result.length === cities) return result;
    }

    return arr;
  }

  tickets.forEach((ticket) => {
    const prev = flights.get(ticket[0]);
    flights.set(ticket[0], prev ? [...prev, ticket[1]] : [ticket[1]]);
  });

  flights.forEach((flight) => flight.sort());

  const result = dfs(['ICN'], flights, 1);

  return result;
}
