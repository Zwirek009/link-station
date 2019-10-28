import unittest
from linkstation.link_station import Point, LinkStation, Device

class TestPoint(unittest.TestCase):
    
    def test_get_distance_to(self):
        """
        Test get_distance_to method.
        """
        data = [
            Point(0,0),
            Point(3,4)
        ]
        
        result = data[0].get_distance_to(data[1])

        self.assertEqual(result, 5)

class TestLinkStation(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.station = LinkStation(10, 10, 15)

    def test_get_power_in_reach(self):
        """
        Test get_power_in_reach method for Point that is in reach of selected linkstation.
        """
        point = Point(20, 20)

        result = self.station.get_power(point)

        self.assertAlmostEqual(result, 0.7359313)

    def test_get_power_not_in_reach(self):
        """
        Test get_power_in_reach method for Point that is not in reach of selected linkstation.
        """
        point = Point(20, 22)

        result = self.station.get_power(point)

        self.assertEqual(result, 0)

class TestDevice(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.stations = [
            LinkStation(21, 0, 15),
            LinkStation(0, 13, 22),
            LinkStation(20, 12, 1)
        ]
    
    def test_get_best_link_station_with_power_available(self):
        """
        Test get_best_link_station_with_power method when any station is available.
        """
        device = Device(21, 13)

        result = device.get_best_link_station_with_power(self.stations)

        self.assertEqual(result, "Best link station for point 21,13 is 21,0 with power 4.0\n")

    def test_get_best_link_station_with_power_not_available(self):
        """
        Test get_best_link_station_with_power method when no station is available.
        """
        device = Device(123, 34)

        result = device.get_best_link_station_with_power(self.stations)

        self.assertEqual(result, "No link station within reach for point 123,34\n")

if __name__ == '__main__':
    unittest.main()