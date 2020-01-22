from typing import Dict, List

weather_forecasts: Dict[str, dict] = {
    "2020-01-01" : { "temp": 50.7, "rain": False }
}

outfits: List[dict] = [
    {
        'jacket': 'mountain warehouse',
        'img': '/jacket/mountain-warehouse.jpg',
        'good_for': ['cold', 'rain'],
        'temp_range': [30.0, 50.0],
    }
]

def get_forecast(date: str) -> dict:
    return weather_forecasts.get(date)