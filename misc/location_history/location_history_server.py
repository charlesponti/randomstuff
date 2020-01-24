# I created this when I was thinking about what
# it would look like if my devices automatically
# went into dark mode when I entered my home

import time


class Device:
    def get_location():
        return {"lat": 5.345, "lng": 10.567, "is_near_home": True}

    def update_position():
        current_time = time.time()
        current_location = device.get_location()
        if current_location["is_near_home"]:
            device.turnOnDarkMode()

    def turn_on_dark_mode():
        device.settings.dark_mode = True
        device.ui.reset()


device = Device()
