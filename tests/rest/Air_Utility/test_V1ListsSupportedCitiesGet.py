from scabbard import get_client


def test__v1_lists_supported_cities_get():
    client = get_client()

    supported_cities = client.Air_Utility\
        .V1ListsSupportedCitiesGet(country='US')\
        .result()
    assert 'LTS' == supported_cities['Cities'][0]['code']
