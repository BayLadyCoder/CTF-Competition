def collatz(n):
    if n < 3000:
        if n%2 != 0:
            n = 3*n + 1
            # n = n / 2
        else:
            n = n / 2
            # n = 3*n + 1
        print(n)
        collatz(n)


collatz(1000)
# print(74%2)
# print(74%2 == 0)