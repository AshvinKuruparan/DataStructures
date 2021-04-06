class Queue:
    def __init__(self):
        self.queue = []
    
    def front (self):
        return self.queue[0]

    def dequeue (self):
        hold = self.queue.pop(0)
        return hold

    def enqueue(self, element):
        return self.queue.append(element)

    def is_empty(self):
        return not self.queue

    def __str__(self):
        if self.queue:
            hold = ' '
            for x in range(len(self.queue)):
                hold = hold + str(self.queue[x]) + ' '
            hold ='[' + hold + ']'
        else:
            hold = '[ ]'
        
        return hold

queue = Queue()
print('is_empty():', queue.is_empty())
print('empty:', queue)
queue.enqueue(10)
print('is_empty():', queue.is_empty())
print('empty:', queue)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print('after enqueue(4):', queue)
print('dequeue():', queue.dequeue())
print('dequeue():', queue.dequeue())
print('dequeue():', queue.dequeue())
print('dequeue():', queue.dequeue())