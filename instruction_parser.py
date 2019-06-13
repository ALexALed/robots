import logging

from lark import Lark, Transformer
from lark.exceptions import UnexpectedCharacters

from route import Route
from city_map import CityMap


logger = logging.getLogger(__name__)


ROBOT_GRAMMAR = """
    start: start_expr (turn_expr | go_expr | go_until_expr)*
    start_expr: "start at (" X "," Y ")"
    turn_expr: "turn" TURN_DIRECTION
    go_expr: "go" DIRECTION? BLOCKS_NUMBER "blocks"
    go_until_expr: "go until you reach landmark" LANDMARK_NAME

    TURN_DIRECTION: ("left" | "right")
    LANDMARK_NAME: /"[^"]*"/
    BLOCKS_NUMBER: ("0".."9")+
    X: ("0".."9")+
    Y: ("0".."9")+
    DIRECTION: ("north" | "east" | "south" | "west")
    %import common.WS
    %ignore WS
"""


class RobotTransformer(Transformer):
    def start_expr(self, expr_args):
        x, y = int(expr_args[0].value), int(expr_args[1].value)
        self._current_direction = 'north'
        self._route = Route(start_point=(x, y))

    def turn_expr(self, expr_args):
        direction = expr_args[0].value

        directions = ["north", "east", "south", "west"]
        current_index = directions.index(self._current_direction)
        shift_value = -1 if direction == 'left' else 1
        desired = current_index + shift_value

        # direction calculated from desired turn type
        self._current_direction = directions[desired if desired <= 3 else 0]

    def go_expr(self, expr_args):
        if len(expr_args) == 1:
            direction = self._current_direction
            block_numbers = int(expr_args[0].value)
        else:
            direction = expr_args[0].value
            block_numbers = int(expr_args[1].value)
            self._current_direction = direction

        # need to map cardinal direction to coordinates direction
        coord_direction = 'x' if direction in {'west', 'east'} else 'y'
        steps = (
            -block_numbers if direction in {'south', 'west'} else block_numbers
        )
        self._route.move_in_direction(coord_direction, steps)

    def go_until_expr(self, expr_args):
        landmark = expr_args[0].value
        x, y = CityMap.get_landmark_coordinates_by_name(landmark)
        if x and y:
            self._route.move_to_point(x, y)


parser = Lark(ROBOT_GRAMMAR, parser='lalr', transformer=RobotTransformer())


def create_route(instructions):
    try:
        parser.parse(instructions)
        return True
    except UnexpectedCharacters:
        logger.error('Failed parse instructions')
        return False
