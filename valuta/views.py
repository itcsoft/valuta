from django.shortcuts import render
from .currency_value import currency_EUR, currency_USD, currency_KZT, currency_RUB

# Create your views here.
def home(request):
    return render(request, 'index.html', {
        'USD': currency_USD,
        'EUR': currency_EUR,
        'KZT': currency_KZT,
        'RUB': currency_RUB,
        'converted_usd_result': 0
    })


def convertDollar(request):
    if int(request.POST.get('input_value')) > 0:
        input_value = int(request.POST.get('input_value'))
        converted_usd = input_value / currency_USD

        return render(request, 'index.html', {
            'USD': currency_USD,
            'EUR': currency_EUR,
            'KZT': currency_KZT,
            'RUB': currency_RUB,
            'converted_usd_result': format(converted_usd, '.2f')
        })
