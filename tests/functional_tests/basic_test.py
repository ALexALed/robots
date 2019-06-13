import unittest

from db import db_manager
from instruction_parser import create_route
from route import Route


class RouteTestClass(unittest.TestCase):

    def setUp(self):
        db_manager.TEST_RUN = True
        db_manager.init_db()

    def test_route_x_right(self):
        code = """
        start at (90, 90)
        go east 10 blocks
        """
        create_route(code)
        route = Route.get_last_route()
        steps = [(s.x, s.y) for s in route.steps]
        assert steps[-1] == (100, 90)

    def test_route_x_left(self):
        code = """
        start at (90, 90)
        go west 10 blocks
        """
        create_route(code)
        route = Route.get_last_route()
        steps = [(s.x, s.y) for s in route.steps]
        assert steps[-1] == (80, 90)

    def test_route_y_top(self):
        code = """
        start at (90, 90)
        go north 10 blocks
        """
        create_route(code)
        route = Route.get_last_route()
        steps = [(s.x, s.y) for s in route.steps]
        assert steps[-1] == (90, 100)

    def test_route_y_down(self):
        code = """
        start at (90, 90)
        go south 10 blocks
        """
        create_route(code)
        route = Route.get_last_route()
        steps = [(s.x, s.y) for s in route.steps]
        assert steps[-1] == (90, 80)

    def test_turn_left(self):
        code = """
        start at (90, 90)
        go south 10 blocks
        turn left
        go 10 blocks
        """
        create_route(code)
        route = Route.get_last_route()
        steps = [(s.x, s.y) for s in route.steps]
        assert steps[-1] == (100, 80)

    def test_turn_right(self):
        code = """
        start at (90, 90)
        go south 10 blocks
        turn right
        go 10 blocks
        """
        create_route(code)
        route = Route.get_last_route()
        steps = [(s.x, s.y) for s in route.steps]
        assert steps[-1] == (80, 80)

    def tearDown(self):
        db_manager.remove_db()
