class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # if list is empty (no head), do nothing
        if not self.head: 
            return
        # if current node's next_node is None (i.e., nothing currently comes after it), that node is currently the last in the list and will become the next head
        if node.next_node is None: 
            # reassign list's head to this node
            self.head = node
            # reverse by turning's the new head's next_node value to its old prev value
            node.next_node = prev
            return
        # otherwise: 
        # store current node's next value for recursive call later (will pass in as the next node to reverse)
        next = node.next_node
        # reverse the current node by updating it's next_node value with the prev value that's passed into the function
        node.next_node = prev
        # recursive call -- update next (the current node's old next_node value) and pass in the current node as the prev value
        self.reverse_list(next, node)
