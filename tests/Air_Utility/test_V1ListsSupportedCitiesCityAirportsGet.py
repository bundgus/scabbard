from scabbard import get_client


def test__v1_lists_supported_cities_city_airports_get():
    client = get_client()

    airports = client.Air_Utility\
        .V1ListsSupportedCitiesCityAirportsGet(city='NYC')\
        .result()
    assert 'JFK' == airports['Airports'][0]['code']
