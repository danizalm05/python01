# -*- coding: utf-8 -*-
"""
The phonenumbers library will only return the country name.
 Using OpenCage geocoder will translate the country name to the
 position (the center of the country). 
 At no point does either library or service know where you are.
Original file is located at
    https://colab.research.google.com/drive/1BZOPkH-VRd3CX9-nmPdxVyDvTHfxszWN

 pip install   phonenumbers
 pip install   opencage
 pip  install folium
"""

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import opencage
from opencage.geocoder import OpenCageGeocode
import folium

number ="+972542052810"
#www.opencagedata.com   create account and get API key

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber,'en')

service_pro =  phonenumbers.parse(number)
service = carrier.name_for_number(pepnumber,'en')

print ("location = ",location,"  Provider name =  ",service)

key ='660b765a1d04425e893f4e86bb2a9e93'

geocoder = OpenCageGeocode(key)

query = str(location)
results = geocoder.geocode(location)
print(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

myMap  =  folium.Map(location=[lat,lng],zoom_start = 9) 
folium.Marker([lat,lng],popup=location).add_to(myMap)
myMap.save("mylocation.html")


 