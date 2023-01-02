arr_inp = [int(x) for x in input().split()]


def list_is_sorted_or_not(arr):
    if len(arr) == 1 or len(arr) == 0:
        return True

    if arr[0] > arr[1]:
        return False

    return list_is_sorted_or_not(arr[1:])


print(list_is_sorted_or_not(arr_inp))
