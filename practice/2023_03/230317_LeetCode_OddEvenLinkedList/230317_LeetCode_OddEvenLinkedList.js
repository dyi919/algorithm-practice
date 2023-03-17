// https://leetcode.com/problems/odd-even-linked-list/description/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
let oddEvenList = function (head) {
  if (!head) return head;

  let odd = head;
  let even = head.next;

  while (odd.next && odd.next.next) {
    let temp = odd.next;

    odd.next = odd.next.next;
    odd = odd.next;
    temp.next = odd.next;
  }

  odd.next = even;

  return head;
};
