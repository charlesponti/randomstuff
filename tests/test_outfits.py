from misc.outfits import weather_forecasts, get_forecast


def test_get_weather():
    date = "2020-01-01"
    assert get_forecast(date) == weather_forecasts[date]


def test_no_weather_data():
    assert get_forecast("2020-01-02") is None
