import scabbard

client = scabbard.get_client()

countries = client.Air_Utility.V1ListsSupportedCountriesGet(pointofsalecountry='NZ').result()

print('PointOfSale')
print(countries['PointOfSale'])

print('OriginCountries')
for c in countries.OriginCountries:
    print(c['CountryCode'], c['CountryName'])

print('DestinationCountries')
for c in countries.DestinationCountries:
    print(c['CountryCode'], c['CountryName'])

print('Links')
for l in countries.Links:
    print(l['rel'])
    print(l['href'])
