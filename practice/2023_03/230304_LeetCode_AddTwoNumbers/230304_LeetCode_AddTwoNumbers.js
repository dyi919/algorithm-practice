/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
let addTwoNumbers = function (l1, l2) {
  let head = new ListNode();
  let cur = head;
  let sum = 0;
  let carry = 0;

  while (l1 || l2 || sum > 0) {
    sum += (l1?.val ?? 0) + (l2?.val ?? 0);

    if (sum >= 10) {
      carry = 1;
      sum -= 10;
    }

    cur.val = sum;

    l1 = l1?.next;
    l2 = l2?.next;

    if (l1 || l2 || carry > 0) {
      cur.next = new ListNode();
      cur = cur.next;
    }

    sum = carry;
    carry = 0;
  }

  return head;
};
