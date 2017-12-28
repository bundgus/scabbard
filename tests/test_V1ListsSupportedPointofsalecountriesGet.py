from scabbard import get_client


def test__v1_lists_supported_countries_get():
    client = get_client()

    countries = client.Air_Utility.V1ListsSupportedPointofsalecountriesGet().result()
    # should be at least one entry with a string 2 characters long
    assert 2 == len(countries.Countries[0].CountryCode)
