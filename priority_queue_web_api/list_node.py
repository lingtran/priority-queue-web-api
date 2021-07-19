from .models import Job


class ListNode:
    
    def __init__(self, data: Job=None, next=None) -> None:
        self._data = data if data else None
        self._next = next if next else None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data) -> None:
        self._data = data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next) -> None:
        self._next = next
