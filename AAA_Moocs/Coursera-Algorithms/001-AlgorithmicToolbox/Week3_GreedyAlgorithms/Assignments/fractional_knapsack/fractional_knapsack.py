# Uses python3
import sys
import operator

def get_optimal_value(capacity, weights, values):
    value = 0.
    taken = []
    # print(weights)
    # print(values)
    # calculate the per unit value for the items
    values_pUnit = [v / w for w, v in zip(weights, values)]


    # print(values_pUnit)
    # find index of max value
    while capacity > 0:
        # get index of max valued item
        index,_ = max(enumerate(values_pUnit), key=operator.itemgetter(1))
        # check if amount of possible weight from this item is 
        take = min(weights[index], capacity)
        # print('value currently at:', value, 'now adding', take*values_pUnit[index])
        value += take  * values_pUnit[index]
        # print('after adding the value is:', value)
        # update trackers
        taken.append(values[index])
        capacity -= take
        values_pUnit[index] = 0

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))


# data = (50, [60,100,120], [20, 50, 30])
# # n, capacity = data[0:2]
# capacity = data[0]
# values = data[1]
# weights = data[2]
# print(get_optimal_value(capacity, weights, values))