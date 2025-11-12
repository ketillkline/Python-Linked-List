class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def display(self):
        current = self.head
        node_list = []
        while current:
            node_list.append(current.data)
            current = current.next
        formatted_text = ' --> '.join(node for node in node_list)
        print(formatted_text)

    def delete_node(self, data):
        current = self.head
        previous = None
        if data == self.head.data:
            self.head = self.head.next
            return
        while current and data != current.data:
            previous = current
            current = current.next
        if not current:
            print(f"ERROR: Data '{data}' not found")
            return
        previous.next = current.next
