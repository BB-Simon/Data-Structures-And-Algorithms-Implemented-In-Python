from linked_list import DoubleLinkedList


class Stack:
    def __init__(self):
        # self.__internal_list = []
        self.__list = DoubleLinkedList()

    def push(self, value):
        # self.__internal_list.append(value)
        self.__list.add(value)

    def pop(self):
        value = self.__list.back()
        self.__list.remove_last()
        return value

    def is_empty(self):
        return self.__list.size == 0

    def peek(self):
        return self.__list.back()

    def __len__(self):
        # return len(self.__internal_list)
        return self.__list.size


my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack.peek())
my_stack.push(5)
print(len(my_stack))
print(my_stack.pop())
print(len(my_stack))
print(my_stack.peek())
