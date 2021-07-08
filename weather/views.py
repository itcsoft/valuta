from django.shortcuts import render
import requests

pogoda_api_key = 'fa0c69065a227aae0ae1081d5953bcfa'

pogoda_url = 'https://api.openweathermap.org/data/2.5/weather?q={city},{state}&lang=ru&appid={api_key}&units=metric'


def current_weather(request):
    weathers = {
        'osh': 36.4,
        'bishkek': 31.4,
        'london': 24.5
    }
    return render(request, 'weather_template.html', {
        'osh':  weathers['osh'],
        'bishkek': weathers['bishkek']
    })


def weather_online(request):
    return render(request, 'weather_online.html')


def get_weather_online(request):
    city_for_url = request.POST.get('city_input')
    state_for_url = request.POST.get('state_input')
    
    pogoda_url_final = pogoda_url.format(
        city = city_for_url, 
        state = state_for_url, 
        api_key = pogoda_api_key
    )

    pogo_otvet = requests.get(pogoda_url_final)
    pogo_otvet_json = pogo_otvet.json()

    temp = pogo_otvet_json['main']['temp']

    return render(request, 'weather_online.html', {
        'pogoda_otvet': pogo_otvet_json,
        'temperature': temp,
        'city_for_url': city_for_url
    })