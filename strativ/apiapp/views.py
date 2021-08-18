from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    responses = requests.get('https://restcountries.eu/rest/v2/all').json()

    context = {
        'responses': responses
    }

    return render(request, "apiapp/index.html", context)
