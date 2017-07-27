# Uses python3
import sys

def get_majority_element(a, left, right):
    a.sort()
    mid = (len(a)//2)

    if len(a)%2 == 0:
        median = a[mid]
        if (median == a[left] or median == a[right]):
            return 1
        else:
            return 0
    else:

        medianL = a[mid]
        medianR = a[mid+1]
        if (median == a[left] or median == a[right]):



if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
