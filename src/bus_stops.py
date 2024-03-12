def number(bus_stops):
    remaining_passengers = 0

    for on, off in bus_stops:
        #remaining_passengers = remaining_passengers + on
        #remaining_passengers = remaining_passengers - off
        remaining_passengers += on - off
    return remaining_passengers

