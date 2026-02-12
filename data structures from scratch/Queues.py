class Queue:
    def __init__(self):
        self._queue = []
        
    def enqueue(self, item):
        self._queue.append(item)
    
    def dequeue(self):
        if self.isEmpty(self._queue):
            return "Empty queue"
        return self._queue.pop(0)
        
    def peek(self):
        if self.isEmpty(self._queue):
            return "Empty queue"
        return self._queue[0]
    
    def size(self):
        return len(self._queue)
    
    def isEmpty(self):
        return len(self._queue) == 0

    def show(self):
        print(self._queue)

        

my_queue = Queue()
my_queue.enqueue("A")
my_queue.enqueue("B")
my_queue.enqueue("C")
my_queue.enqueue("D")

print(my_queue)
my_queue.show()
