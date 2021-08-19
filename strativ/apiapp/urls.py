from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:country_id>", views.country, name="country"),
    path("search/", views.search, name="search"),
]
