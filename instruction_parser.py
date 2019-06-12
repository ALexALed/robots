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
    def start_expr(self, args):
        x, y = args[0], args[1]
        self._current_direction = 'north'
        self._route = Route(start_point=(x, y))

    def turn_expr(self, args):
        direction = args[0]
        self._current_direction = direction

    def go_expr(self, args):
        if len(args) == 1:
            direction = self._current_direction
            block_numbers = args[0]
        else:
            direction = args[0]
            block_numbers = args[1]

        direction = 'x' if direction in {'west', 'east'} else 'y'
        self._route.add_step(direction, block_numbers)

    def go_until_expr(self, args):
        landmark = args[0]
        CityMap.get_landmark_by_name




parser = Lark(ROBOT_GRAMMAR, parser='lalr', transformer=RobotTransformer())

def run_robot(instructions):
    try:
        parser.parse(instructions)
        return True
    except UnexpectedCharacters:
        logger.error('Failed parse instructions')
        return False

def main():
    code = """
    start at (245, 161)
    go north 5 blocks
    turn right
    go until you reach landmark "Statue of Old Man with Large Hat"
    go west 25 blocks
    turn left
    got 3 blocks
    """
    run_robot(code)

if __name__ == '__main__':
    main()