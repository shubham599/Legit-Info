# Python Code
# get_api_data.py

from django.core.management.base import BaseCommand, CommandError
from cfc_app.models import Location, Impact
from cfc_app.Legiscan_API import Legiscan_API

class Command(BaseCommand):
    help = 'For each state in the United States listed under LOCATIONS, '
    help +='this script will fetch the most recent legislative session, '
    help +='and create a json output file under /sources/NN.json where, '
    help +='NN is the two-letter state abbreviation like AZ or OH.'

    def handle(self, *args, **options):
        usa = Location.objects.get(shortname='usa')
        locations = Location.objects.order_by('hierarchy').filter(parent=usa)

        leg = Legiscan_API()
        print(leg.url)
        for loc in locations:
            state = loc.shortname.upper()  # Convert state to UPPER CASE
            print('Fetching for state: {} -- {}'.format(state,loc.desc))
            leg.getAllBills(state)

        # self.stdout.write('This was extremely simple!!!')
