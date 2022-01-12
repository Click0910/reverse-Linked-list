class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_list:

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:

            node = Node(nodes[0])
            self.head = node
            for i in range(1, len(nodes)):
                node.next = Node(i+1)
                node = node.next

    def print_list(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


l_list = Linked_list([1, 2, 3, 4, 5])
l_list.print_list()
l_list.reverse()

