class QueueData:
    def __init__(self, max_size):
        self.max_size = max_size
        self.data = [0] * self.max_size
        self.size = 0
        self.front_pointer = 0
        self.rear_pointer = -1

    def __repr__(self) -> str:
        return_str = ""
        ptr = self.front_pointer
        while ptr != (self.rear_pointer + 1) % self.max_size: 
            return_str += str(self.data[ptr]) + " "
            ptr = (ptr + 1) % self.max_size
        return return_str
            
def is_empty(q):
    return q.size == 0

def is_full(q):
    return q.max_size == q.size

def enqueue(item, q):
    if not is_full(q):
        q.rear_pointer = (q.rear_pointer + 1) % q.max_size
        q.size += 1
        q.data[q.rear_pointer] = item
    else:
        print("Queue is full")

def dequeue(q):
    if not is_empty(q):
        item_p = q.front_pointer
        q.front_pointer = (q.front_pointer + 1) % q.max_size
        q.size -= 1
        return q.data[item_p]
    else:
        print("Queue is empty")

new_q1 = QueueData(5)
new_q2 = QueueData(7)

for num in range(11, 15):
    enqueue(num, new_q1)

for num in range(101, 106):
    enqueue(num, new_q2)

print(new_q1)
print(new_q2)

enqueue(15, new_q1)
enqueue(16, new_q1)
enqueue(150, new_q1)

enqueue(160, new_q2)

print(new_q1)
print(new_q2)

for _ in range(6):
    print(dequeue(new_q1))

for _ in range(8):
    print(dequeue(new_q2))

print(new_q1)
print(new_q2)

enqueue(20, new_q1)
enqueue(200, new_q2)

print(new_q1)
print(new_q2)
print(new_q1)
