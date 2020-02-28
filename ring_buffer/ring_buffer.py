from typing import Union
from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.current = self.storage.head

    def append(self, item: Union[str, int]):
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        else:
            self.current = self.current.next or self.storage.head
            self.current.value = item

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        self.tracker = self.storage.head
        while self.tracker:
            list_buffer_contents.append(self.tracker.value)
            self.tracker = self.tracker.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
