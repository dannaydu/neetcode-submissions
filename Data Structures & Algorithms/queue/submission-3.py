class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        return self.head.next == self.tail
        

    def append(self, value: int) -> None:
        new = Node(value)
        last = self.tail.prev

        last.next = new
        new.prev = last
        new.next = self.tail
        self.tail.prev = new
        

    def appendleft(self, value: int) -> None:
        new = Node(value)
        first = self.head.next

        first.prev = new
        new.next = first
        new.prev = self.head
        self.head.next = new
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        last = self.tail.prev
        val = last.value

        new_last = last.prev
        new_last.next = self.tail
        self.tail.prev = new_last

        return val

        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        first = self.head.next
        val = first.value

        new_first = first.next
        new_first.prev = self.head
        self.head.next = new_first
        return val
        
