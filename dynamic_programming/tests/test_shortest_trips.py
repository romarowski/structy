import unittest as ut
from dynamic_programming.shortest_trips import shortest_trips

class TestShortestTrips(ut.TestCase):
    def test_shortest_trips(self):
        n = 5
        expected_output = 2
        self.assertEqual(shortest_trips(n), expected_output)

    def test_zero_trips(self):
        n = 0
        expected_output = 0
        self.assertEqual(shortest_trips(n), expected_output)

    def test_large_number_of_trips(self):
        n = 2017
        expected_output = 673
        self.assertEqual(shortest_trips(n), expected_output)