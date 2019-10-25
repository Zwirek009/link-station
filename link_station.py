"""This module calculates best link station (with most power) for a device at given point (x,y)"""

# TODO
def get_power(point, link_station):
    """Get power from given link_station (x, y, reach) for given point (x, y)"""
    raise NotImplementedError

# TODO
def get_best_link_station(point, link_stations):
    """Get best link station (with most power) for given point (x,y)"""
    return "TODO get_best_link_station for point" + str(point)


def main():
    """Run program for exercise data"""
    # initialize data
    link_stations = [
        (0, 0, 10),
        (20, 20, 5),
        (10, 0, 12)
    ]
    points = [
        (0, 0),
        (100, 100),
        (15, 10),
        (18, 18)
    ]

    # calculate best link stations and print the results
    # TODO consider making calculations concurrent
    for point in points:
        print("Best link station for point" + str(point) + " is " + \
        get_best_link_station(point, link_stations))

    print("DONE")

if __name__ == "__main__":
    main()
