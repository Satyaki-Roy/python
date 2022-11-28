from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 7)


def getCompressedString(input):
    final_str = ''
    current_chr = ''
    current_chr_count = 0
    for c in input:
        if current_chr == '':
            current_chr = c
            current_chr_count = 1
        else:
            if c == current_chr:
                current_chr_count += 1
            else:
                if current_chr_count > 1:
                    final_str += current_chr + str(current_chr_count)
                else:
                    final_str += current_chr
                current_chr = c
                current_chr_count = 1
    if current_chr_count > 1:
        final_str += current_chr + str(current_chr_count)
    else:
        final_str += current_chr
    return final_str


# Main.
string = stdin.readline().strip();
ans = getCompressedString(string)
print(ans)
