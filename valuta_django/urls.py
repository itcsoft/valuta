"""valuta_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from valuta import views as valutaViews
from weather import views as weatherViews


urlpatterns = [
    path('', valutaViews.home),
    path('convert-usd/', valutaViews.convertDollar),
    path('admin/', admin.site.urls),
    
    path('get-weather/', weatherViews.current_weather),
    path('weather-online/', weatherViews.weather_online),
    path('get-weather-online/', weatherViews.get_weather_online)
]
