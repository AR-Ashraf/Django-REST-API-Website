from django.core.management.base import BaseCommand
import requests
from apiapp.models import ApiApp


class Command(BaseCommand):
    help = 'Fetches Data From API.'

    def handle(self, *args, **kwargs):

        responses = requests.get('https://restcountries.eu/rest/v2/all').json()

        print("Please Wait...")

        for response in responses:
            try:
                ApiApp(
                    name=response["name"],
                    alpha2code=response["alpha2Code"],
                    alpha3code=response["alpha3Code"],
                    capital=response["capital"],
                    population=response["population"],
                    timezones=response["timezones"],
                    languages=response["languages"],
                    borders=response["borders"]
                ).save()
            except Exception as ex:
                print(ex)
        self.stdout.write("Action Completed!")
