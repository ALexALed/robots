import operator
import logging

from city_map import CityMap
from db.db_manager import RouteModel

logger = logging.getLogger(__name__)


class Route:
    '''
    Represents route object
    Store route to database
    '''

    def __init__(self, start_point=(0, 0)):
        self.current_point = start_point
        self._steps = [start_point]

        self._route_db = RouteModel.save_route()
        self._route_db.save_step(*start_point)

    def move_in_direction(self, direction, steps):
        current_x, current_y = self.current_point
        desired_steps = steps

        if desired_steps < 0:
            step_value = -1
        else:
            step_value = 1

        while desired_steps != 0:
            if direction == 'x':
                current_x += step_value
            else:
                current_y += step_value

            desired_steps -= step_value

            self.add_step(current_x, current_y)

        self.current_point = (current_x, current_y)

    def move_to_point(self, x, y):
        current_x, current_y = self.current_point

        if x < current_x:
            operator_to_apply = operator.sub
        elif x > current_x:
            operator_to_apply = operator.add

        while x != current_x:
            current_x = operator_to_apply(current_x, 1)
            self.add_step(current_x, current_y)

        if y < current_y:
            operator_to_apply = operator.sub
        elif y > current_y:
            operator_to_apply = operator.add

        while y != current_y:
            current_y = operator_to_apply(current_y, 1)
            self.add_step(current_x, current_y)

        self.current_point = (current_x, current_y)

    def add_step(self, x, y):
        if CityMap.is_move_allowed(x, y):
            self._steps.append((x, y))
            self._route_db.save_step(x, y)
        else:
            logger.error('Step does not correct!')

    @staticmethod
    def get_last_route():
        return RouteModel.select().order_by(RouteModel.id.desc()).get()
