// https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

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
function deleteDuplicates(head) {
    let dummy = new ListNode(-Infinity, head);
    let prev = dummy;
    let cur = head;

    while (cur?.next) {
        if (cur.val === cur.next.val) {
            while (cur.next && cur.val === cur.next.val) {
                cur.next = cur.next.next;
            }
            prev.next = cur.next;
            cur = cur.next;
        } else {
            prev.next = cur;
            cur = cur.next;
            prev = prev.next;
        }
    }

    return dummy.next;
};