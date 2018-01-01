from scabbard import get_client


def test__v1_lists_supported_countries_get():
    client = get_client()

    countries = client.Air_Utility\
        .V1ListsSupportedCountriesGet(pointofsalecountry='NZ')\
        .result()
    assert 'NZ' == countries.PointOfSale
