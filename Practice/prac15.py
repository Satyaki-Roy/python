## Read input as specified in the question.
## Print output as specified in the question.

def printLeader(n_input, arr_input):
    rev_arr = arr_input[::-1]
    current_min = rev_arr[0]
    rev_final_arr = [str(rev_arr[0])]

    for e in rev_arr[1:]:
        if current_min < e:
            rev_final_arr.append(str(e))
            current_min = e
        elif current_min == e:
            rev_final_arr.append(str(e))
        else:
            pass

    final_arr = rev_final_arr[::-1]

    print(' '.join(final_arr))


# Taking Input Using Fast I/O
def takeInput():
    n_input = int(input())

    if n_input == 0:
        return list(), 0

    arr_input = [int(x) for x in input().strip().split(" ")]
    return arr_input, n_input


# main
arr, n = takeInput()
printLeader(n, arr)

# for i in range(n_input):
#     leader = arr_input[i]
#     for j in arr_input[i + 1:]:
#         if arr_input[i] < j:
#             leader = ''
#     if leader != '':
#         final_arr.append(str(leader))
