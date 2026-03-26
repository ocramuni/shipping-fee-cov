def shipping_cost(weight, destination, is_express, is_fragile):
    if weight <= 0:
        raise ValueError("weight must be positive")

    cost = 5

    if weight > 10:
        cost += 10
    elif weight > 5:
        cost += 5

    if destination == "international":
        cost += 15
    elif destination != "domestic":
        raise ValueError("unknown destination")

    if is_express:
        cost += 12

    if is_fragile and weight > 8:
        cost += 7

    return cost