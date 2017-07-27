"""
Implements a greedy Algorithmic Solution to the fractional Knapsack optimization problem.

input: 
- A list of weight value pairs for individual items
- A maximum capacity of our knapsack W

Return:
- a list of fractional amounts of items that maximize overall value at max Capacity
"""
import operator

def fractionalKnapsack(items, capacity):
    """
    Given a dict of item:value pairs, and a max Weight return the best fractional combination
    """

    # For each item, calculate its unit value

    # sort items in ascending unit order

    # for all items, combine the maximum possible amount of the highest per unit valued item

    # if there is still room available, try to fill the rest with the next max unit valued item

    current_weight = 0
    unit_values = {value:value/weight for weight, value in items.items()}
    print(unit_values)

    packed_items = {}
    package_value = 0
    rest_capacity = capacity
    # Sort values in ascending order based on unit prices
    value_sorted_items = sorted(items.items(), key=lambda x: x[1] / x[0], reverse=False)
    # print(value_sorted_items)
    while value_sorted_items:
        # Iterate over the greedy choice until the capacity is maxed out
        weight,value = value_sorted_items.pop()
        value = unit_values[value]
        
        # check for available capacity
        print('adding {} amount of {}'.format(min(rest_capacity, weight), value))
        packed_items.update({value : min(rest_capacity, weight)})

        # recalculate the current_weight
        current_weight = sum(packed_items.values())
        rest_capacity = capacity - current_weight

    packed_value = sum([weight* value for weight,value in packed_items.items()])

    print(packed_value, packed_items)




items = {
    20:20,
    5:10,
    4:20,
}



fractionalKnapsack(items, 10)