print(n) = $(n)
fib(a, b) = print(a), c = b, b = a, a = +(a, c)
loop(a, b) = fib(a, b), >(a, 233, print("DONE")), <(a, 234, loop(a, b))
loop(1, 0)