
weather_forecasts = [
    { 'day': '2020-01-01', 'temp': 50.7, 'rain': False }
]

outfits = [
    {
        'jacket': 'mountain warehouse',
        'img': '/jacket/mountain-warehouse.jpg',
        'good_for': ['cold', 'rain'],
        'temp_range': [30.0, 50.0],
    }
]

def get_suitable_outfit(date: str):
    return weather_forecasts[date]

print(get_suitable_outfit())