class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def printList(head):
    # Utility function to print the doubly linked list
    while head:
        print(head.data, end=" ")
        head = head.next
    print()

def reverseDLL(head):
    if head == None:
        return None
    if head.next == None:
        return head

    curr = head
    prev = None
    while curr != None:
        prev = curr
        curr.next, curr.prev = curr.prev, curr.next
        curr = curr.prev
    return prev

head = Node(2)
second = Node(4)
third = Node(5)
head.next = second
second.prev = head
second.next = third
third.prev = second

# Example 1:
printList(head)
reverseDLL(head)
printList(head)