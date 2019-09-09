# 斐波那契数列


# def fib(n):
#     i = j = 1
#     for k in range(1, n+1):
#         print(i, end=' ')
#         i, j = j, i+j
#
#
# fib(11)


def fib(n):
    if n == 1 or n == 2:
        return 1
    if n > 2:
        return fib(n-1) + fib(n-2)


for i in range(1, 21):
    print(fib(i), end=",")
