a = 10 #any len of the fibonachi series

def fib():
    f1, f2 = 0, 1

    while True:
        yield f1
        f1, f2 = f2, f1+f2

for i, f in zip(range(a+1), fib()):
    print('{i:3}: {f:3}'.format(i=i, f=f))