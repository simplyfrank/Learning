# Uses python3
import sys

def get_change(m):
    coins = [1,5,10]
    
    # Store the value yet to be changed
    value = m
    change = []
    # get max number for either coin or current value
    while value > 0:
        # check what the biggest coin is that is below the rest value
        for coin in sorted(coins, reverse=True):
            while int(value / coin) > 0:
                value -= coin
                change.append(coin)
            # divide by coin and if the integer value is above > 0 keep it
    return len(change)
if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

# print(get_change(268))
