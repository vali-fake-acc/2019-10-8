from sys import argv
import time

def f(n):
    global steps
    steps += 1
    if n > 4:
        a = n//2 - 1
        b = n%2
        x1 = f(a)
        x2 = f(a+1)
        if b:
            x3 = x1 + x2
            x4 = x2 + x3
        else:
            x3 = x2
            x4 = x1 + x2
        return x1 * x3 + x2 * x4
        # same as: return f(a) * f(a+b+1) + f(a+1) * f(a+b+2)
        # but faster
    elif n > 1:
        return n-1
    elif n == 1:
        return 1

steps = 0
t = time.time()
n = int(argv[1])
print(f'Result: {f(n)}')
print(f'Time: {(time.time() -t):.5f}s')
print(f'Steps: {steps}')
print(f'N: {n}')

