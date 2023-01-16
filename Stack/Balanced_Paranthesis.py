from sys import stdin
from queue import LifoQueue


# def isBalanced(expression):
#     q = LifoQueue()
#     for i in expression:
#         if i == '(':
#             q.put('(')
#         else:
#             if q.empty():
#                 return False
#             q.get()
#     return q.empty()


def isBalanced(expression):
    q = []
    for i in expression:
        if i == '(':
            q.append('(')
        else:
            if len(q) == 0:
                return False
            q.pop()
    return len(q) == 0


# main
expression = stdin.readline().strip()

if isBalanced(expression):
    print("true")
else:
    print("false")
