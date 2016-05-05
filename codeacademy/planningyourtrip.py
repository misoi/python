def hotel_cost(nights):
    x=140*nights
    return x

#getting there

def plane_ride_cost(city):
    if city=="Charlotte":
        return 183
    elif city=="Tampa":
        return 220
    elif city=="Pittsburgh":
        return 222
    else:
        return 475
