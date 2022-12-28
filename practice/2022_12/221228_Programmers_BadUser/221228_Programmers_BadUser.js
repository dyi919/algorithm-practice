// school.programmers.co.kr/learn/courses/30/lessons/64064

https: function parseRegExp(banned_id) {
  const _ban = banned_id.replaceAll('*', '.');
  return new RegExp(`^${_ban}$`, 'g');
}

function parseString(ban_list) {
  return ban_list.sort().join('');
}

function solution(user_id, banned_id) {
  let visited = Array(8).fill(false);
  let combinations = new Set();

  function createCombination(banned_idx, count, ban_list) {
    if (count === banned_id.length) {
      combinations.add(parseString(ban_list));
      return;
    }

    if (banned_idx === banned_id.length) return;

    const re = parseRegExp(banned_id[banned_idx]);

    for (let i = 0; i < user_id.length; i++) {
      if (visited[i]) continue;

      const result = user_id[i].match(re);

      if (result) {
        visited[i] = true;
        createCombination(banned_idx + 1, count + 1, [...ban_list, result[0]]);
        visited[i] = false;
      }
    }
  }

  createCombination(0, 0, []);

  return combinations.size;
}
