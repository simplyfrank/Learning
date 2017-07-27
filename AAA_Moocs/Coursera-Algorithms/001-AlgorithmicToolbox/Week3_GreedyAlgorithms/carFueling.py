def carfueling(goal, stations, capacity=300):
    """
    Takes a goal at distance n, a list of gas stations that can be used along the way
    and the capacity of the gas tank for our car.

    Returns: the minimum list of gas stations to take to reach the goal
    """
    # Tank defines the 
    pos = 0
    tanking_stops = []

    while pos < goal-capacity:
        # pick the maximum reachable distance
        distance_to_gst = [station - pos for station in stations]
        # check if we can reach them
        reachable = [station for station in distance_to_gst if station < capacity ]
        if reachable:
            # drive to furthest reachable station
            next_stop = max(reachable)
            tanking_stops.append(next_stop + pos)
            pos += next_stop + 1
        else:
            # ran out of gas
            print('Ran out of gas before reaching the goal')
            return False
    print('reached the goal')
    print (tanking_stops)


stations = [250, 375, 675, 720, 775, 830, 960, 1170]

carfueling(1180, stations)