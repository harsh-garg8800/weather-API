from rest_framework.views import APIView
from .serializers import DropDownCitySerializer,CheckWeatherSerializer,CityUpdateSerializer, CreateCitySerializer, DeleteCitySerializer
from rest_framework import status
from rest_framework.response import Response
from .models import CityName
# Create your views here.

# Get Dropdown city view
class GetDropView(APIView):
    serializer_class = DropDownCitySerializer

    def get(self, request):
        serializer = DropDownCitySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        status_code = status.HTTP_200_OK
        return Response(
            {'success': 'True', 'city' : serializer.data['dropdown_city']}, status=status_code)  


#create city view
class CreateCityView(APIView):
    serializer_class = CreateCitySerializer
    def post(self, request):
        serializer = CreateCitySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        status_code = status.HTTP_200_OK
        return Response({'success': 'True', 'message': 'City created successfully'}, status=status_code)


# Get city View
class GetCityView(APIView):
    def get(self,request):
        final_response= [{'id':i.id, 'city':i.city,}for i in CityName.objects.all()]
        return Response(final_response)

#update city view
class CityUpdateView(APIView):
    serializer_class = CityUpdateSerializer
    def post(self, request):
        serializer = CityUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        status_code = status.HTTP_200_OK
        return Response({'success': 'True', 'message': 'City updated successfully'}, status=status_code)


# Get weather view
class GetweatherView(APIView):
    serializer_class = CheckWeatherSerializer

    def post(self, request):
        serializer = CheckWeatherSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        status_code = status.HTTP_200_OK
        return Response(
            {'success': 'True', 'data' : serializer.data['data']}, status=status_code)


# Delete city view
class CityDeleteView(APIView):
    serializer_class = DeleteCitySerializer
    def post(self, request):
        serializer = DeleteCitySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        status_code = status.HTTP_200_OK
        return Response({'success': 'True', 'message': 'City deleted successfully'}, status=status_code)
