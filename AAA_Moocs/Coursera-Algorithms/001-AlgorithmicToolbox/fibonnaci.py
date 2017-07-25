

# Naive Implementation of the fibonacci sequence
def fibonnaci(n):
    if n <= 1:
        return n
    else:
        return  fibonnaci(n-1) + fibonnaci(n-2)




# More efficient implementation
def fibonacci_2(n):
    result = [0 for a in range(n+1)]
    result[0] = 0
    result[1] = 1
    for i in range(2,n+1):
        result[i] = result[i-1] + result[i-2]
    return result[n]

print(fibonacci_2(10000))