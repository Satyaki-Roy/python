from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildTree(postOrder, inOrder, n):
    if n == 0:
        return None

    root_of_bt = postOrder[-1]
    root_node_of_bt = BinaryTreeNode(root_of_bt)
    index_of_root_in_inOrder = inOrder.index(root_of_bt)

    leftPostOrder = postOrder[0:index_of_root_in_inOrder]
    rightPostOrder = postOrder[index_of_root_in_inOrder:n - 1]
    leftInOrder = inOrder[0:index_of_root_in_inOrder]
    rightInOrder = inOrder[index_of_root_in_inOrder + 1:]

    left_bt = buildTree(leftPostOrder, leftInOrder, len(leftPostOrder))
    right_bt = buildTree(rightPostOrder, rightInOrder, len(rightPostOrder))

    root_node_of_bt.left = left_bt
    root_node_of_bt.right = right_bt

    return root_node_of_bt


'''-------------------------- Utility Functions --------------------------'''


def printLevelWise(root):
    if root is None:
        return

    pendingNodes = queue.Queue()
    pendingNodes.put(root)
    pendingNodes.put(None)

    while not pendingNodes.empty():
        frontNode = pendingNodes.get()

        if frontNode is None:
            print()

            if not pendingNodes.empty():
                pendingNodes.put(None)

        else:
            print(frontNode.data, end=" ")

            if frontNode.left is not None:
                pendingNodes.put(frontNode.left)

            if frontNode.right is not None:
                pendingNodes.put(frontNode.right)


# Taking level-order input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0:
        return list(), list(), 0

    postOrder = list(map(int, stdin.readline().strip().split(" ")))
    inOrder = list(map(int, stdin.readline().strip().split(" ")))

    return postOrder, inOrder, n


# Main
postOrder, inOrder, n = takeInput()
root = buildTree(postOrder, inOrder, n)
printLevelWise(root)
