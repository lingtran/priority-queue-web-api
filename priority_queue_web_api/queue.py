
from .models import Job
from .list_node import ListNode


class Queue:
    
    def __init__(self, head: ListNode=None, tail: ListNode=None) -> None:
        self._head = head if head else None
        self._tail = tail if tail else None
        self._count = 0

    @property
    def head(self) -> ListNode:
        return self._head
    
    @head.setter
    def head(self, head: ListNode):
        self._head = head

    @property
    def tail(self) -> ListNode:
        return self._tail

    @tail.setter
    def tail(self, tail: ListNode):
        self._tail = tail

    @property
    def count(self) -> int:
        return self._count
    
    @count.setter
    def count(self, value):
        self._value = value

    #TODO:// refactor to queue by priority (head - lowest number, tail - highest number)
    def enqueue(self, job: Job) -> None:
        next = ListNode(data=job)
        if self.head is None:
            self.head = next
            self.tail = self.head
        else:
            self.tail.next = next
            self.tail = next
        self.count+=1

    def dequeue(self) -> None:
        if self.head is not None:
            self.head = self.head.next
            self.count-=1

queue = Queue()
