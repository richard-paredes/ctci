'''
An animal shelter, which holds only dogs and cats, operates on a strictly
FIFO basis. They must adopt either the oldest of whichever, or select a type
and receive the oldest animal of that type. Create the data structure to maintain
this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat. You can use the built in linked list data structure.
'''

from random import randint

class Node:
    def __init__(self, value):
        self.value == value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def add(self, value):
        node = Node(value)
        if self.tail is None:
            self.tail = node
        else:
            current_tail = self.tail
            current_tail.next = node
            node.prev = current_tail
            self.tail = node
        
        if self.head is None:
            self.head = self.tail
        self.size += 1

    def remove_from_head(self):
        if self.head is None:
            raise Exception("List is empty")
        
        if self.head == self.tail:
            self.head, self.tail = None, None
        else:
            self.head = self.head.next
        self.size -= 1

    def remove_from_tail(self):
        if self.tail is None:
            raise Exception("List is empty")
        
        if self.tail == self.head:
            self.head, self.tail = None, None
        else:
            self.tail = self.tail.prev
        self.size -= 1

class AnimalShelter:
    def __init__(self):
        self.cats = None
        self.dogs = None

    def enqueue_cat(self, cat):
        self.cats.add(cat)
    
    def enqueue_dog(self, dog):
        self.dogs.add(dog)
    
    def dequeueAny(self):
        if self.dogs.is_empty() and self.cats.is_empty():
            raise Exception("No animals available")
        
        if self.dogs.is_empty():
            return self.dequeueCat()
        if self.cats.is_empty():
            return self.dequeueDog()
        
        if randint() % 2 == 0:
            return self.dequeueDog()
        return self.dequeueCat()

    def dequeueDog(self):
        if self.dogs.is_empty():
            raise Exception("No dogs available")
        return self.dogs.remove_from_head()
    
    def dequeueCat(self):
        if self.cats.is_empty():
            raise Exception("No cats available")
        return self.cats.remove_from_head()

def solution(n):
    return False

def main():
    for test_case in []:
        print(solution(test_case))

if __name__ == "__main__":
    main()