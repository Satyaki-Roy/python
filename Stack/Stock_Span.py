from sys import stdin


# def stockSpan(price, n):
#     stock_span = []
#     stack = []
#     for i in price:
#         # print(i)
#         # print(stack)
#         if len(stock_span) == 0:
#             stock_span.append(1)
#             stack.append(i)
#         elif i > stack[-1]:
#             stack.append(i)
#             count = 0
#             replica_stack = []
#             replica_stack.extend(stack)
#             pop_ele = None
#             last_pop_ele = None
#             while len(replica_stack) != 0:
#                 if last_pop_ele is None:
#                     last_pop_ele = pop_ele
#                 if pop_ele is None:
#                     pop_ele = replica_stack.pop()
#                     count += 1
#                 else:
#                     pop_ele = replica_stack.pop()
#                     if last_pop_ele <= pop_ele:
#                         break
#                     else:
#                         count += 1
#             stock_span.append(count)
#         elif i <= stack[-1]:
#             stack.append(i)
#             stock_span.append(1)
#     return stock_span


def stockSpan(price, n):
    stock_span = [0 for i in range(n)]
    stock_span[0] = 1
    st = [0]

    for i in range(1, n):
        while len(st) > 0 and price[st[-1]] < price[i]:
            st.pop()

        stock_span[i] = i + 1 if len(st) == 0 else i - st[-1]

        st.append(i)

    return stock_span


'''-------------- Utility Functions --------------'''


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")

    print()


def takeInput():
    size = int(stdin.readline().strip())

    if size == 0:
        return list(), 0

    price = list(map(int, stdin.readline().strip().split(" ")))

    return price, size


# main
price, n = takeInput()

output = stockSpan(price, n)
printList(output)
