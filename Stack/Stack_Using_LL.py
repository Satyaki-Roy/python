from sys import stdin


# Following is the structure of the node class for a Singly Linked List
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.__data = None
        self.__head = None
        self.__count = 0

    '''----------------- Public Functions of Stack -----------------'''

    def getSize(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0

    def push(self, data):
        if self.isEmpty():
            self.__data = Node(data)
            self.__head = self.__data
            self.__count = 1
        else:
            new_node = Node(data)
            new_node.next = self.__head
            self.__head = new_node
            self.__count += 1

    def pop(self):
        if self.isEmpty():
            return -1
        delete_node = self.__head
        new_head = self.__head.next
        self.__head.next = None
        self.__head = new_head
        self.__count -= 1
        return delete_node.data

    def top(self):
        if self.isEmpty():
            return -1
        return self.__head.data


# main
q = int(stdin.readline().strip())

stack = Stack()

while q > 0:

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1:
        data = int(inputs[1])
        stack.push(data)

    elif choice == 2:
        print(stack.pop())

    elif choice == 3:
        print(stack.top())

    elif choice == 4:
        print(stack.getSize())

    else:
        if stack.isEmpty():
            print("true")
        else:
            print("false")

    q -= 1
