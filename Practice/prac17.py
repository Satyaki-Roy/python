# Write your code here
# To take space separated input for two variables, we use the following syntax (3 lines)
x, n = input().split()
x = int(x)
n = int(n)


def raise_to_power(x_input, n_input):
    if n_input == 0:
        return 1
    small_output = raise_to_power(x_input, n_input - 1)
    return x_input * small_output


print(raise_to_power(x, n))
