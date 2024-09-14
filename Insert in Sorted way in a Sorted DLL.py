"""Given a sorted doubly linked list and an element x, you need to insert the element x into the correct position in the sorted Doubly linked list(DLL).

Note: The DLL is sorted in ascending order

Example:

Input: LinkedList: 3->5->8->10->12 , x = 9

Output: 3->5->8->9->10->12

Explanation: Here node 9 is inserted in the Doubly Linked-List.
Input: LinkedList: 1->4->10->11 , x = 15

Output: 1->4->10->11->15

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).

Constraints:
1 <= number of nodes <= 103
1 <= node -> data , x <= 104"""


class Solution:
    # Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
        newnode = Node(x)

        # Case 1: If the list is empty, the new node becomes the head
        if head == None:
            return newnode

        curr = head

        # Case 2: If the new node should be inserted at the head (smallest value)
        if x < head.data:
            newnode.next = head
            head.prev = newnode
            return newnode

        # Traverse the list to find the correct position
        while curr != None:
            # Case 3: Insert before a node where the new node's value is smaller
            if x < curr.data:
                lastnode = curr.prev
                lastnode.next = newnode
                newnode.prev = lastnode

                newnode.next = curr
                curr.prev = newnode
                return head  # Return after inserting the node

            # Move to the next node
            if curr.next == None:  # Case 4: Inserting at the end of the list
                curr.next = newnode
                newnode.prev = curr
                return head

            curr = curr.next