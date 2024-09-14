"""Given a doubly-linked list, a position p, and an integer x. The task is to add a new node with value x at the position just after pth node in the doubly linked list.

Example 1:

Input:
LinkedList: 2<->4<->5
p = 2, x = 6
Output: 2 4 5 6
Explanation: p = 2, and x = 6. So, 6 is
inserted after p, i.e, at position 3
(0-based indexing).
Example 2:

Input:
LinkedList: 1<->2<->3<->4
p = 0, x = 44
Output: 1 44 2 3 4
Explanation: p = 0, and x = 44 . So, 44
is inserted after p, i.e, at position 1
(0-based indexing).
Your Task:
The task is to complete the function addNode() which head reference, position and data to be inserted as the arguments, with no return type.

Expected Time Complexity : O(N)
Expected Auxilliary Space : O(1)

Constraints:
1 <= N <= 104
0 <= p < N"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Function to insert a new node after the p-th node in a doubly linked list
def addNode(head, p, data):
    # Step 1: Create the new node with the given data
    new_node = Node(data)

    # Step 2: Traverse the list to the p-th node
    curr = head
    for i in range(p):
        if curr is None:
            return  # If position is out of bounds, do nothing
        curr = curr.next

    # Step 3: Insert the new node after the p-th node
    next_node = curr.next
    curr.next = new_node
    new_node.prev = curr

    if next_node is not None:
        new_node.next = next_node
        next_node.prev = new_node


# Example usage:
def printList(head):
    # Utility function to print the doubly linked list
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


# Creating a doubly linked list 2 <-> 4 <-> 5
head = Node(2)
second = Node(4)
third = Node(5)
head.next = second
second.prev = head
second.next = third
third.prev = second

# Example 1:
printList(head)
addNode(head, 1, 6)
printList(head)  # Output: 2 4 5 6

# Creating another doubly linked list 1 <-> 2 <-> 3 <-> 4
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
head.next = second
second.prev = head
second.next = third
third.prev = second
third.next = fourth
fourth.prev = third

# Example 2:
printList(head)
addNode(head, 0, 44)
printList(head)  # Output: 1 44 2 3 4


