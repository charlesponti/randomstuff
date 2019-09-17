
class Device:
  def getLocation():
    return {
      'lat': 5.345,
      'lng': 10.567,
      'is_near_home': True
    }

  def update_position():
    currentLocation = device.getLocation()
    if currentLocation['is_near_home']:
      device.turnOnDarkMode()

device = Device()

