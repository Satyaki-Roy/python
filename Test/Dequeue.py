from sys import stdin


# Following is the structure of the node class for a Double Linked List
class Node:

    def __init__(self, data):
        self.previous = None
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.__tail = None
        self.__data = None
        self.__head = None
        self.__count = 0

    '''----------------- Public Functions of Stack -----------------'''

    def getSize(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0

    def insertFront(self, data):
        if self.getSize() == 10:
            return -1
        new_node = Node(data)

        if self.isEmpty():
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.next = self.__head
            self.__head.previous = new_node
            self.__head = new_node

        self.__count += 1

    def insertRear(self, data):
        if self.getSize() == 10:
            return -1
        new_node = Node(data)

        if self.isEmpty():
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node
            new_node.previous = self.__tail
            self.__tail = new_node

        self.__count += 1

    def deleteFront(self):
        if self.isEmpty():
            return -1

        node_to_be_removed = self.__head
        self.__head = self.__head.next

        node_to_be_removed.next = None

        self.__count -= 1

        # return node_to_be_removed.data

    def deleteRear(self):
        if self.isEmpty():
            return -1

        node_to_be_removed = self.__tail
        self.__tail = self.__tail.previous

        node_to_be_removed.previous = None

        self.__count -= 1

        # return node_to_be_removed.data

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.__head.data

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.__tail.data


# main
inputs = [int(x) for x in stdin.readline().strip().split(" ")]

my_queue = Queue()

i = 0

while i <= len(inputs) - 2:

    choice = inputs[i]

    if choice == 1:
        i += 1
        data = inputs[i]
        if my_queue.insertFront(data) is not None:
            print(-1)

    elif choice == 2:
        i += 1
        data = inputs[i]
        if my_queue.insertRear(data) is not None:
            print(-1)

    elif choice == 3:
        if my_queue.deleteFront() is not None:
            print(-1)

    elif choice == 4:
        if my_queue.deleteRear() is not None:
            print(-1)

    elif choice == 5:
        print(my_queue.getFront())

    elif choice == 6:
        print(my_queue.getRear())

    i += 1
