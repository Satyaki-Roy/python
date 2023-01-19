class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def take_input():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    root_left = take_input()
    root_right = take_input()
    root.left = root_left
    root.right = root_right
    return root


def print_btn(root):
    if root is None:
        return
    data = root.data
    left = root.left.data if root.left is not None else ' '
    right = root.right.data if root.right is not None else ' '
    print(data, ':', left, right)
    print_btn(root.left)
    print_btn(root.right)


def num_of_nodes(root):
    if root is None:
        return 0
    return 1 + num_of_nodes(root.left) + num_of_nodes(root.right)


root_input = take_input()
print_btn(root_input)
print(num_of_nodes(root_input))
