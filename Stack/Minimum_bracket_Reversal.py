from sys import stdin


def countBracketReversals(inputString):
    st = []
    count = 0
    for i in inputString:
        if i == '{':
            st.append('{')
        else:
            if len(st) != 0 and st[-1] == '{':
                st.pop()
            else:
                st.append('{')
                count += 1
    if len(st) % 2 == 0:
        return (len(st) // 2) + count
    else:
        return -1


# main
print(countBracketReversals(stdin.readline().strip()))
