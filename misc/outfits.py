
weather_forecasts = [
    { 'date': '2020-01-01', 'temp': 50.7, 'rain': False }
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
    for forecast in weather_forecasts:
        if forecast['date'] == date:
            return forecast

print(get_suitable_outfit('2020-01-01'))