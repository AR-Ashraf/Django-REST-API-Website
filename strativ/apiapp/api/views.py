from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from apiapp.models import ApiApp
from apiapp.api.serializers import CountrySerializer, CountryUpdateSerializer, CountryCreateSerializer

SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'


# Urls:
# 		1) List of all countries: http://127.0.0.1:8000/api/country/list
# 		2) Detail of a specific country: http://127.0.0.1:8000/api/country/list?search=<name of country>
# 		3) Create a new country: http://127.0.0.1:8000/api/country/create
# 		4) Update an existing country: http://127.0.0.1:8000/api/country/<country_name>/update
# 		5) Delete an existing country: http://127.0.0.1:8000/api/country/<country_name>/delete


class ApiCountryListView(ListAPIView):
    queryset = ApiApp.objects.all()
    serializer_class = CountrySerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'capital', 'population', 'languages', 'borders')


@api_view(['PUT'])
def api_update_country_view(request, country_name):
    print(request.data)
    try:
        country = ApiApp.objects.get(name=country_name)
    except ApiApp.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        print(request.data)
        serializer = CountryUpdateSerializer(country, data=request.data, partial=True)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = UPDATE_SUCCESS
            data['name'] = country.name
            data['alpha2code'] = country.alpha2code
            data['alpha3code'] = country.alpha3code
            data['capital'] = country.capital
            data['population'] = country.population
            data['timezones'] = country.timezones
            data['languages'] = country.languages
            data['borders'] = country.borders
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def api_create_country_view(request):
    if request.method == 'POST':
        data = request.data
        print(data)
        serializer = CountryCreateSerializer(data=data)

        data = {}
        if serializer.is_valid():
            country = serializer.save()
            data['response'] = CREATE_SUCCESS
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def api_delete_country_view(request, country_name):
    try:
        country = ApiApp.objects.get(name=country_name)
    except ApiApp.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = country.delete()
        data = {}
        if operation:
            data['response'] = DELETE_SUCCESS
        return Response(data=data)
