class Landmark:
    '''
    Represents landmark data
    '''
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


class CityMap:
    '''
    Represents City Map
    City map is global for application
    '''
    size_x = 250
    size_y = 250
    _landmarks = []

    @classmethod
    def put_landmark(cls, name, x, y):
        cls._landmarks.append(Landmark(name, x, y))

    @classmethod
    def get_landmark_coordinates_by_name(cls, name):
        for l in cls._landmarks:
            if l.name == name:
                return (l.x, l.y)

        return (None, None)

    @classmethod
    def is_move_allowed(cls, x, y):
        if not (0 < x < cls.size_x or 0 < y < cls.size_y):
            return False

        return True
