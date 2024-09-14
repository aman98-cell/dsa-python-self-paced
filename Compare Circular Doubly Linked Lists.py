"""Given two circular doubly linked lists of sizes n1 and n2 respectively, the task is check if the corresponding elements of the lists are same or not.
The tail of a circular doubly linked list is connected to head via its next pointer, and the previous pointer of head is connected to the tail.

Example 1:

Input:
LinkedList1: 1
LinkedList2: 1
Output: 1
Example 2:

Input:
LinkedList1: 2<->5<->7<->8<->99<->100
LinkedList2: 7<->8<->9<->73<->2
Output: 0
Your Task:
The task is to complete the function compareCLL() which takes head1 and head2 references as an arguments. The function should return true if all the corresponding elements of the lists are same, else it should return false. (The driver's code print 1 if the returned value is true, otherwise false.)

Expected Time Complexity: O(n1 + n2).
Expected Auxiliary Space: O(1).

Constraints:
1 <= number of nodes <= 10^5"""


class Solution:
    def compareCLL(self, head1, head2):
        # Edge cases: if one list is empty and the other is not, they can't be the same
        if head1 is None and head2 is None:
            return True  # Both lists are empty
        if head1 is None or head2 is None:
            return False  # One list is empty, but the other isn't

        # Start from the head of both lists
        curr1 = head1
        curr2 = head2

        # Traverse both lists and compare corresponding elements
        while True:
            # If the data at current nodes are different, return False
            if curr1.data != curr2.data:
                return False

            # Move to the next node in both lists
            curr1 = curr1.next
            curr2 = curr2.next

            # If we have come back to the head of either list, we must check if
            # both lists are at their respective head (meaning equal lengths)
            if curr1 == head1 and curr2 == head2:
                return True  # Both lists are circular and ended at the same time

            # If one list reaches back to the head but the other does not, lengths are unequal
            if (curr1 == head1 and curr2 != head2) or (curr1 != head1 and curr2 == head2):
                return False


