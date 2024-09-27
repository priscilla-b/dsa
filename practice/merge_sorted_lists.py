class Node:
    # creating a node
    def __init__(self, data):
        self.data = data
        self.next = None


    # insertion at beginning of node
    def insert_at_start(self, data):
        new_node = Node(data)  # create a new node with the given data
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

node = Node(30)
node.insert_at_start(12)
print(node)