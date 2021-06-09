# from collections import deque

from linked_list import DoubleLinkedList


class Queue:
    def __init__(self):
        self.__list = DoubleLinkedList()

    def enque(self, value):
        self.__list.add(value)

    def deque(self):
        value = self.__list.front()
        self.__list.remove_first()
        return value

    def is_empty(self):
        return self.__list.size == 0

    def front(self):
        return self.__list.front()

    def __len__(self):
        return self.__list.size


# my_queue = Queue()
# print(len(my_queue))
# my_queue.enque(1)
# my_queue.enque(7)
# my_queue.enque(10)
# print(len(my_queue))
# print(my_queue.front())
# print(my_queue.deque())
# print(my_queue.front())
