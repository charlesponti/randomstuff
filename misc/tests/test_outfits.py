import unittest
from outfits import weather_forecasts, get_forecast

class TestOutfits(unittest.TestCase):
    def test_get_weather(self):
        date = '2020-01-01'
        self.assertEqual(get_forecast(date), weather_forecasts[date])