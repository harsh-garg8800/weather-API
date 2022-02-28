from django.urls import path
from .views import GetDropView,GetweatherView,CityUpdateView,CreateCityView,CityDeleteView,GetCityView

urlpatterns = [
    path('dropdowncity', GetDropView.as_view() ),
    path('weather', GetweatherView.as_view() ),
    path('createcity',CreateCityView.as_view()),
    path('updatecity',CityUpdateView.as_view()),
    path('deletecity',CityDeleteView.as_view()),
    path('getcity',GetCityView.as_view())
]