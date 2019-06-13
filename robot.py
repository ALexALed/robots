class Robot:
    def __init__(self, name):
        self.name = name

    def follow_route(self, route):
        steps_done = []

        for step in route.steps:
            steps_done.append((step.x, step.y))

        return steps_done
