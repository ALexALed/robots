import unittest
from unittest.mock import MagicMock

from robot import Robot
from collections import namedtuple


class RobotTestClass(unittest.TestCase):

    def test_robot_move(self):
        Point = namedtuple('Point', ['x', 'y'])
        test_points = [Point(80, 80), Point(80, 81), Point(80, 83)]
        test_route = MagicMock()
        test_route.steps = test_points
        steps = Robot(name='test').follow_route(test_route)
        self.assertListEqual(steps, test_points)
