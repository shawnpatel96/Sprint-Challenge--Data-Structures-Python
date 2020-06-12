# from doublyLinkedList import DoublyLinkedList
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_node = 0
        self.storage = [None] * capacity

    def append(self, item):
        self.storage[self.current_node] = item
        self.current_node += 1
        # if capacity full 
        if self.current_node >= self.capacity:
            # reset node to 0
            self.current_node = 0

    def get(self):
        # Return all items not equal to none
        return [item for item in self.storage if item != None]