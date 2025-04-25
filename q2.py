class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("QUEUE IS EMPTY")
            return
        print(self.front.data)
        self.front = self.front.next
        if self.front is None:
            self.rear = None

    def peek(self):
        if self.front is None:
            print("QUEUE IS EMPTY")
            return
        print(self.front.data)

    def is_empty(self):
        return self.front is None

if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.dequeue()
    q.dequeue()
    print(q.is_empty())
    q.peek()
    q.dequeue()
    q.dequeue()
    q.peek()
    print(q.is_empty())
