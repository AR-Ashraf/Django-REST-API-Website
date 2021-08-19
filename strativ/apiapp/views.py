from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render
from .models import ApiApp


# Create your views here.
@login_required(login_url='login')
def index(request):
    context = {
        'apiapp': ApiApp.objects.all()
    }

    return render(request, "apiapp/index.html", context)

@login_required(login_url='login')
def country(request, country_id):
    try:
        country = ApiApp.objects.get(pk=country_id)
    except ApiApp.DoesNotExist:
        raise Http404("Country Does Not Exist")
    context = {
        "country": country
    }
    return render(request, "apiapp/country.html", context)

@login_required(login_url='login')
def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        country = ApiApp.objects.filter(name__contains=search)
        context = {
            'country': country
        }
        return render(request, "apiapp/search.html", context)
