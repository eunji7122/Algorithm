import math


def method(A, K):
    max_num = max(A)
    minus = num_len(max_num)

    for i in range(len(A)):
        if i % K == 0:
            line_print(K, minus)

        print('|', end='')
        for k in range(minus - num_len(A[i])):
            print(' ', end='')
        print(A[i], end='')

        if i % K == K-1:
            print('|', end='')
            print()

    if len(A) % K == 0:
        line_print(K, minus)
    else:
        print('|', end='')
        print()
        line_print(len(A) % K, minus)


def num_len(num):
    return int(math.log10(num) + 1)


def line_print(K, minus):
    for i in range(1, K + 1):
        print('+', end='')
        for j in range(minus):
            print('-', end='')

    print('+')


method([4, 35, 130, 50, 100, 56, 5], 4)
