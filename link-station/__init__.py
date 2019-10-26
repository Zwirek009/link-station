"""This module calculates best link station (with most power) for a device at given point (x,y)"""

import azure.functions as func
import logging
import math

class Point:
    """
    Point class represents a point in 2-dimensional (x,y) space.

    Attributes:
        x (float): x coordinate
        y (float): y coordinate
    """

    def __init__(self, x, y):
        """
        The constructor for Point class.

        Parameters:
            x (float): x coordinate
            y (float): y coordinate
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Defines printable output for the class.

        Returns:
            string: Coordinates of the point in (x,y) format
        """
        return f"{self.x},{self.y}"

    def get_distance_to(self, other):
        """
        Get distance to given Point.

        Parameters:
            other (Point): Point to get distance to

        Returns:
            int: Distance to given Point
        """
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

class Device(Point):
    """
    Device class represents device that resides at some coordinates.

    Inherits from Point class.
    """
    __doc__ += Point.__doc__

    def _str_best_link_station_with_power(self, best_station, power):
        """
        Format pretty string describing best link station with its power.

        Parameters:
            best_station (LinkStation): Best (with most power) for device
            power (float): Power of best station for the device

        Returns:
            string: Pretty string describing best link station with its power
        """
        if power:
            return f"Best link station for point {self} is " + \
                f"{best_station} with power {power}\n"
        return f"No link station within reach for point {self}\n"

    def get_best_link_station_with_power(self, link_stations):
        """
        Get best link station (with most power) for this device.

        Parameters:
            link_stations (LinkStation[]): List of available link stations

        Returns:
            string: Pretty string describing best link station with its power
        """
        best_power = 0
        best_station = link_stations[0]
        for station in link_stations:
            power = station.get_power(self)
            if power > best_power:
                best_station = station
                best_power = power
        return self._str_best_link_station_with_power(best_station, best_power)

class LinkStation(Point):
    """
    LinkStation class represents link station that resides at some coordinates.

    Inherits from Point class.

    Arguments:
        reach (float): Reach of the link station
    """
    __doc__ += Point.__doc__

    def get_power(self, point):
        """
        Get power for given point.

        Parameters:
            point (Point): Point to calculate station power

        Returns:
            float: Power for given point
        """
        distance = self.get_distance_to(point)
        return (self.reach - distance)**2 if distance < self.reach else 0

    def __init__(self, x, y, reach):
        """
        The constructor for LinkStation class.

        Parameters:
            x (float): x coordinate
            y (float): y coordinate
            reach (fleat): Reach of the link station
        """
        Point.__init__(self, x, y)
        self.reach = reach

def run_for_default_data():
    """Run program for exercise data"""
    # initialize data
    link_stations = [
        LinkStation(0, 0, 10),
        LinkStation(20, 20, 5),
        LinkStation(10, 0, 12)
    ]
    devices = [
        Device(0, 0),
        Device(100, 100),
        Device(15, 10),
        Device(18, 18)
    ]

    results = ""
    # calculate best link stations and get the results
    for device in devices:
        results += device.get_best_link_station_with_power(link_stations)
    
    return results 

def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    Execute program on as Azure Function.
    """
    logging.info("BestLinkStation HTTP triggered.")
    return func.HttpResponse(run_for_default_data())

def local_main():
    """
    Execute program locally.
    """
    print(run_for_default_data())

if __name__ == "__main__":
    local_main()
