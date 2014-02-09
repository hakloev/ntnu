mem = {}

def fib(n):
    for k in  range(1, n +1):
        if k <= 2:
            f = 1
        else:
            f = mem[k -1] + mem.pop(k -2, None)
        mem[k] = f
    return mem[n]

print fib(160)
print 'kjor'
