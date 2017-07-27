# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    result = [0 for i in range(n+1)]
    result[0] = 0
    result[1] = 1
    for i in range(2, n+1):
        result[i] = (result[i-1] + result[i-2]) % 10
    return result[i]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
