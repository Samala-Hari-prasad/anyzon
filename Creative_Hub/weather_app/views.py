from django.shortcuts import render

CITIES = [
    {'name': 'Mumbai', 'temp': '31°C', 'condition': 'Humid & Hazy', 'icon': '🌫️', 'humidity': '82%', 'wind': '18 km/h'},
    {'name': 'Delhi', 'temp': '22°C', 'condition': 'Partly Cloudy', 'icon': '⛅', 'humidity': '55%', 'wind': '12 km/h'},
    {'name': 'Bengaluru', 'temp': '26°C', 'condition': 'Pleasant', 'icon': '🌤️', 'humidity': '60%', 'wind': '10 km/h'},
    {'name': 'Chennai', 'temp': '34°C', 'condition': 'Hot & Sunny', 'icon': '☀️', 'humidity': '75%', 'wind': '20 km/h'},
    {'name': 'Kolkata', 'temp': '29°C', 'condition': 'Cloudy', 'icon': '🌥️', 'humidity': '70%', 'wind': '15 km/h'},
    {'name': 'Hyderabad', 'temp': '28°C', 'condition': 'Clear', 'icon': '☀️', 'humidity': '50%', 'wind': '8 km/h'},
    {'name': 'Jaipur', 'temp': '25°C', 'condition': 'Windy', 'icon': '💨', 'humidity': '35%', 'wind': '22 km/h'},
    {'name': 'Pune', 'temp': '27°C', 'condition': 'Mild', 'icon': '🌤️', 'humidity': '58%', 'wind': '11 km/h'},
]

def index(request):
    city_query = request.GET.get('city', '')
    cities = [c for c in CITIES if city_query.lower() in c['name'].lower()] if city_query else CITIES
    return render(request, 'weather_app/index.html', {'cities': cities, 'city_query': city_query})
