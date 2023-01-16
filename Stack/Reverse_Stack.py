from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


def reverseStack(inputStack, extraStack):
    if isEmpty(inputStack):
        return

    element = inputStack.pop()

    reverseStack(inputStack, extraStack)

    while len(inputStack):
        remove = inputStack.pop()
        extraStack.append(remove)

    inputStack.append(element)

    while len(extraStack):
        remove = extraStack.pop()
        inputStack.append(remove)


'''-------------- Utility Functions --------------'''


# Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack):
    return len(stack) == 0


# Taking input using fast I/o method
def takeInput():
    size = int(stdin.readline().strip())
    inputStack = list()

    if size == 0:
        return inputStack

    values = list(map(int, stdin.readline().strip().split(" ")))
    inputStack = values

    return inputStack


# Main
inputStack = takeInput()
emptyStack = list()

reverseStack(inputStack, emptyStack)

while not isEmpty(inputStack):
    print(inputStack.pop(), end=" ")
