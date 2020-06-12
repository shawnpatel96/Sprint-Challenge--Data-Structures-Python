# from doublyLinkedList import DoublyLinkedList
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.storage = []
        self.order = []

    def append(self, item):

        if self.size < self.capacity:
            self.order.append(item)
            self.storage.append(item)
            self.size +=1
        else:
            index = self.order.index(self.storage[0])
            self.storage.pop(0)
            self.order[index] = item
            self.storage.append(item)
                

    def get(self):
        return self.order