from instruction_parser import create_route
from db.db_manager import init_db
from robot import Robot
from route import Route


def main():
    init_db()

    user_choice = input(
        '''
            You can create routes and run robots in this app.
            The city map size 250 x 250 by default

            Please select mode:
                1. Predefined route (will be used system predefined route)
                2. User Input
            Anything else for exit
        '''
    )

    if int(user_choice) == 1:
        code = """
        start at (90, 90)
        go north 5 blocks
        turn right
        go west 25 blocks
        turn left
        go 3 blocks
        """
        create_route(code)
        route = Route.get_last_route()
        bender = Robot('Bender')
        steps = bender.follow_route(route)
        for x, y in steps:
            print('x={} y={}'.format(x, y))

    elif int(user_choice) == 2:
        command = input('>')
        route_created = create_route(command)
        if route_created:
            route = Route.get_last_route()
            bender = Robot('Bender')
            steps = bender.follow_route(route)
            for x, y in steps:
                print('x={} y={}'.format(x, y))
        else:
            print('Route errors')

    else:
        print('Good bye')


if __name__ == '__main__':
    main()
