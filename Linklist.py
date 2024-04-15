import math
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            self.size = 1
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)
            self.size += 1
    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=' ')
            current = current.next
        print()

    def insert(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            current_index = 0
            while current and current_index < index - 1:
                current = current.next
                current_index += 1
            if current:
                new_node.next = current.next
                current.next = new_node

    def remove(self, value):
        current = self.head
        prev = None
        while current:
            if current.value == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next
    def mean(self):
        if not self.head:
            return 0
        total_sum = 0
        current = self.head
        while current:
            total_sum += current.value
            current = current.next
        return total_sum / self.size
    def variance(self):
        if not self.head:
            return 0
        mean = self.mean()
        variance_sum = 0
        current = self.head
        while current:
            variance_sum += (current.value - mean) ** 2
            current = current.next
        return variance_sum / (self.size - 1)
    def standard_deviation(self):
        return math.sqrt(self.variance())