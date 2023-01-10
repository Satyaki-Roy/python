class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def take_input():
    input_data_arr = [int(x) for x in input().split()]
    head = None

    for data in input_data_arr:
        if data == -1:
            break
        new_node = Node(data)
        if head is None:
            head = new_node
        else:
            current_node = head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    return head


head_of_ll = take_input()


def printLL(head):
    curr = head
    while curr is not None:
        print(curr, curr.data, curr.next)
        curr = curr.next


printLL(head_of_ll)
