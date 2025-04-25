class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("NULL")

if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_node(10)
    sll.insert_node(20)
    sll.insert_node(30)
    sll.insert_node(40)
    sll.insert_node(50)
    
    print("Linked List:", end=" ")
    sll.print_list()
