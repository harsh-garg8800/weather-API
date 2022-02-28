from asyncore import write
from django.conf import settings
from rest_framework import serializers
from cities_light.models import City
import urllib.request
import json
import datetime
from .models import CityName
api_key ='a30afa91f57f00db454e4c5308ca2e98'


# serilizer to get the city of US, CA and IN from the GeoNames Database
class DropDownCitySerializer(serializers.Serializer):
    dropdown_city = serializers.ListField(read_only=True)
    
    def validate(self,data):
        dropdown_city = []

        city = City.objects.all()
        get_data=[{'name':i.name} for i in city]

        for i in get_data:
            get_city= i['name']
            if get_city not in dropdown_city:
                dropdown_city.append(get_city)
        return({'dropdown_city':dropdown_city})

# create city
class CreateCitySerializer(serializers.Serializer):
    city = serializers.CharField(max_length = 100, write_only = True)
    def validate(self,data):
        city = data.get("city",None)
        data = CityName.objects.create(city=city)
        return True


# update city
class CityUpdateSerializer(serializers.Serializer):
    city_id = serializers.CharField(write_only = True)
    city = serializers.CharField(write_only = True)
    def validate(self,data):
        city_id = data.get("city_id",None)
        city = data.get("city",None)
        try:
            if not CityName.objects.filter(id=city_id).exists():
                raise serializers.ValidationError("city you are looking for is not exist")
            CityName.objects.filter(id = city_id).update(city=city)  
        except:
            raise serializers.ValidationError("Unable to update the city may be the city you are looking for is not exist")
        return True     


# Get Weather condition according to the city      
class CheckWeatherSerializer(serializers.Serializer):
    City = serializers.CharField(max_length = 100, write_only = True)
    data = serializers.ListField(read_only = True)
    def validate(self,data):
        city = data.get("City",None)
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/forecast?q='+city+'&cnt='+str(4)+'&appid='+api_key).read()

        list_of_data =json.loads(source)
        curr_date = datetime.datetime.now().date()
        curr_day = curr_date.strftime("%A")
        full_data =[]
        for d in list_of_data["list"]:
            c = d['main']
            g = d['weather']
            temp = {'temp':round(c['temp']-273.15,2),'weather':g[0]['description'],'date':curr_date,'day':curr_day}
            if curr_date == datetime.datetime.now().date():
                temp["time"]='today'
            curr_date+=datetime.timedelta(days=1)
            curr_day = curr_date.strftime("%A")
            full_data.append(temp)
        return{'data':full_data}
            

# Delete City
class DeleteCitySerializer(serializers.Serializer):
    city_id = serializers.CharField(write_only = True)
    def validate(self,data):
        city_id = data.get("city_id",None)
        if not CityName.objects.filter(id=city_id).exists():
            raise serializers.ValidationError("city you are looking for is not exist")
        CityName.objects.filter(id = city_id).delete()
        return True


