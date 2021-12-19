

class Queue:

    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        return self.queue[0]

    def size_queue(self):
        return len(self.queue)


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)


print(f'Dequeue: {q.dequeue()}')
