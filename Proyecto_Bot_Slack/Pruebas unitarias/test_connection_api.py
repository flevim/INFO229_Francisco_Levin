import pytest
import requests
from geopy.geocoders import Nominatim 

@pytest.mark.parametrize("city",["Valdivia","Osorno","Temuco","sdfsdfsdggsd"])

def test_connection_api(city):
	api_key = "8b1713b635fa5884b391b173b33386c1"
	geolocator = Nominatim(user_agent="geolocation_places")

	loc = geolocator.geocode(city)
	lat, long = loc.latitude, loc.longitude

	url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&exclude=minutely&units=metric&lang=es&appid=%s" % (lat, long, api_key)
	response = requests.get(url)
	assert str(response) == '<Response [200]>'