# Uses python3
def calc_fib(n):
    if n == 0:
        return 0
    result = [0 for i in range(n+1)]
    result[0] = 0
    result[1] = 1
    for i in range(2, n+1):
        result[i] = result[i-1] + result[i-2]
    return result[n]

n = int(input())
print(calc_fib(n))

