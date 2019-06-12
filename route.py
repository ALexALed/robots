class Route:

    def __init__(self, start_point=(0, 0)):
        self.current_point = start_point
        self._steps = [start_point]

    def add_step(self, direction, steps):
        current_x, current_y = self.current_point
        desired_steps = steps
        while desired_steps > 0:
            if direction == 'x':
                current_x += 1
            else:
                current_y += 1

            self._steps.append((current_x, current_y))

            desired_steps -= 1

        self.current_point = (current_x, current_y)

        
