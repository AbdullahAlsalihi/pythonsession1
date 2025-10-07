

'''
Problem: Reverse a Singly Linked List using Recursion - Choose your own list and reverse it recursively
'''

class Node:
    def __init__(self, value):
        self.value = value # where the data going to be stored for the Node
        self.next = None # This is the pointer for the next value

def print_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

def reverse_list(node):
    if node is None or node.next is None:
        return node # for this one, we're checking if the list is empty or it has 1 value

    new_head = reverse_list(node.next) # recursive case for smaller problems

    node.next.next = node # It means that we're making the next node point back to the current node
    node.next = None # that's how you break the original node link

    return new_head

value1 = Node(10)
value2= Node(20)
value3= Node(3)
value4= Node(14)
value5= Node(100)

value1.next = value2
value2.next = value3
value3.next = value4
value4.next = value5

head = value1

print("Original list")
print_list(head)

reversed_head = reverse_list(head)
print("Reversed List")
print_list(reversed_head)