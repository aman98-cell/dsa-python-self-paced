"""Given a Doubly Linked list and a position. The task is to delete a node from a given position (position starts from 1) in a doubly linked list and return the head of the doubly Linked list.

Examples:

Input: LinkedList = 1 <--> 3 <--> 4, x = 3
Output: 1 <--> 3
Explanation: After deleting the node at position 3 (position starts from 1),the linked list will be now as 1 <--> 3.

Input: LinkedList = 1 <--> 5 <--> 2 <--> 9, x = 1
Output: 5 <--> 2 <--> 9
Explanation:

Expected Time Complexity: O(n)
Expected Auxilliary Space: O(1)

Constraints:
2 <= size of the linked list <= 106
1 <= x <= size of the linked list
1 <= node->data <= 104"""


class Solution:
    def delete_node(self, head, x):
        # code here

        if head is None:
            return None

        count = 0
        curr = head
        while curr != None:
            count += 1
            curr = curr.next
        if x > count:
            return head

        if x == 1:
            newhead = head.next
            if newhead.next != None:
                newhead.prev = None
            return newhead

        curr = head
        for i in range(x - 2):
            curr = curr.next

        node_to_delete = curr.next
        rn = node_to_delete.next
        curr.next = rn
        if rn is not None:
            rn.prev = curr

        return head