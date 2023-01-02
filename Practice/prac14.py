## Read input as specified in the question.
## Print output as specified in the question.

s = input()
arr = s.split()
min_word = ''
min_len = 1000

for word in arr:
    if len(word) < min_len:
        min_len = len(word)
        min_word = word

print(min_word)
