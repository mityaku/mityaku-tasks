maxSize = 5
q = [0 for _ in range(maxSize)]
rear = -1
size = 0
maxItems = 10
front = 0

def isEmpty():
    if(size == 0):
        return True
    else:
        return False
    #endif
#endfunction

def isFull():
    if size == maxSize:
        return True
    else: 
        return False
    #endif
#endfunction

def enqueue(item):
    rear = (rear + 1) % maxSize
    q[rear] = item
    size = size + 1
#endprocedure

def dequeue():
    global front
    global size
    global maxSize
    if isEmpty():
        return("Queue is empty")
    else:
        front = (front + 1) % maxSize
        size = size - 1
    return q[front - 1]
#endprocedure
