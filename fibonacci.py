def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


i = True
while i:
    if fib(i) <= 100:
        print(fib(i))

        i += 1

    else:
        i=False
