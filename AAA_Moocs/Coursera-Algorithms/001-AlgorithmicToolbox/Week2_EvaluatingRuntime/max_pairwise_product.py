# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
a = sorted(a)
assert(len(a) == n)


first, second = a.pop(), a.pop()


print(first * second)
