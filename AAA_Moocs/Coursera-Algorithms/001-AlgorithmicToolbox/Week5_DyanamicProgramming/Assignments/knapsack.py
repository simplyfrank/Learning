# Uses python3
import sys

def optimal_weight(W, w):
    # W is capacity of backpack
    # w is list of bars of gold
    c = [0] * (W + 1)

    for i in range(len(w)):
        for j in range(W, w[i] - 1, -1):
            c[j] = max(c[j], c[j - w[i]] + w[i])
    return c[W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))