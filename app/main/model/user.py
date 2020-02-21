class Converter(object):
    def pounds_to_kilograms(self, pounds: int):
        return pounds / 2.205


class User(object):
    """
    :param weight: Weight of user in kilograms
    :type weight: int
    :param height: Height of user in meters
    :type height: int
    :param reading_speed: The words per minute the user can read
    :type reading_speed: int
    """

    weight: int
    height: int
    reading_speed: int

    def __init__(self, *args, weight: int = 0, height: int = 0):
        "Constructor method"
        super().__init__()
        self.weight = weight
        self.height = height
        self.reading_speed = 0

    def update_reading_speed(self, reading_speed: int):
        "Update reading_speed of user"
        self.reading_speed = reading_speed
