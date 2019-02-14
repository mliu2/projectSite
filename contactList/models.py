from django.db import models
import json
import urllib.parse
from decimal import Decimal

from .config import MapBoxConfig

class Contact(models.Model):

    def save(self):
        address = "%s %s, %s %s" % (self.street, self.city, self.state, self.zip)
        self.latitude,self.longitude = self.geocode(address)
        print (self.longitude)
        super(Contact, self).save()

    def geocode(self, address):
        address = urllib.parse.quote_plus(address)
        maps_api_url = '?'.join([
            'https://api.mapbox.com/geocoding/v5/mapbox.places/' + address + '.json',
            urllib.parse.urlencode({'access_token': MapBoxConfig.access_token, 'autocomplete':True})
        ])
        response = urllib.request.urlopen(maps_api_url)
        data = json.loads(response.read().decode('utf8'))
        if 'features' in data:
            longitude = data['features'][0]['geometry']['coordinates'][0]
            latitude = data['features'][0]['geometry']['coordinates'][1]
            return Decimal(latitude),Decimal(longitude)
        else:
            return None, None

    NJ = 'NJ'
    NY = 'NY'
    PA = 'PA'
    CT = 'CT'
    STATE_CHOICES = (
        (NJ, 'New Jersey'),
        (NY, 'New York'),
        (PA, 'Pennsylvania'),
        (CT, 'Connecticut'),
    )
    MR = 'Mr.'
    MS = 'Ms.'
    MRS = 'Mrs.'
    DR = 'Dr.'
    TITLE_CHOICES = (
        (MR,MR),
        (MS,MS),
        (MRS,MRS),
        (DR,DR),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    state = models.CharField(
        max_length=20,
        choices = STATE_CHOICES,
        default = NJ,
    )
    zip = models.CharField(max_length=5)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    title = models.CharField(
        max_length=5,
        choices = TITLE_CHOICES,
        default = MR,
    )
    use_mail = models.BooleanField()
    use_phone = models.BooleanField()
    use_email = models.BooleanField()
    latitude = models.DecimalField(max_digits=8, decimal_places=5,null=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=5,null=True)
