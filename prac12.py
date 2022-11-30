from sys import stdin


def spiralPrint(mat, nRows, mCols):
    row_arr = [x for x in range(nRows)]
    col_arr = [x for x in range(mCols)]
    total_ele = nRows * mCols
    final_arr = []

    while total_ele != 0:
        # first row
        for r in row_arr:
            for c in col_arr:
                final_arr.append(mat[r][c])
                total_ele -= 1
            row_arr.remove(r)
            break

        # last column
        for c in col_arr[::-1]:
            for r in row_arr:
                final_arr.append(mat[r][c])
                total_ele -= 1
            col_arr.remove(c)
            break

        # last row
        for r in row_arr[::-1]:
            for c in col_arr[::-1]:
                final_arr.append(mat[r][c])
                total_ele -= 1
            row_arr.remove(r)
            break

        # first row
        for c in col_arr:
            for r in row_arr[::-1]:
                final_arr.append(mat[r][c])
                total_ele -= 1
            col_arr.remove(c)
            break

    print(' '.join([str(x) for x in final_arr]))


# Taking Input Using Fast I/O
def take2DInput():
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])

    if nRows == 0:
        return list(), 0, 0

    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


# main
t = int(stdin.readline().rstrip())

while t > 0:
    mat, nRows, mCols = take2DInput()
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1
