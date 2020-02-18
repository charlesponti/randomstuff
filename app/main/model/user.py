class User(object):
    """
    :param reading_speed: The words per minute the user can read
    :type reading_speed: int
    """

    reading_speed: int

    def __init__(self):
        super().__init__()
        self.reading_speed = 0

    def update_reading_speed(self, reading_speed: int):
        "Update reading_speed of user"
        self.reading_speed = reading_speed
