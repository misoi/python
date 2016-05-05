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
    # transportation part

    def rental_car_cost(days):
    if days>=7:
        total=(40*days)-50
        return total
    elif days>=3 and days<7:
        total=(40*days)-20
        return total
    else:
        total=(40*days)
        return total

    # pulling them together

    def rental_car_cost(days):
    if days>=7:
        total=(40*days)-50
        return total
    elif days>=3 and days<7:
        total=(40*days)-20
        return total
    else:
        total=(40*days)
        return total
def trip_cost(city,days):
    return hotel_cost(days)+plane_ride_cost(city)+rental_car_cost(days)
