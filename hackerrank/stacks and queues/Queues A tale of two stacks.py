class MyQueue(object):
    def __init__(self):
        self.stackpush = []
        self.stackdelete = []

    def peek(self):
        if not self.stackdelete:
            while self.stackpush:
                self.stackdelete.append(self.stackpush.pop())
        return self.stackdelete[-1]

    def pop(self):
        if not self.stackdelete:
            while self.stackpush:
                self.stackdelete.append(self.stackpush.pop())
        self.stackdelete.pop()

    def put(self, value):
        self.stackpush.append(value)


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())