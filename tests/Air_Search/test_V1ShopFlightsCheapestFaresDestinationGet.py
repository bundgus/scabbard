from scabbard import get_client


def test__v1_shop_flights_cheapest_fares_destination_get():
    client = get_client()

    cheapest_flights = client.Air_Search\
        .V1ShopFlightsCheapestFaresDestinationGet(destination='LAX',
                                                  pointofsalecountry='US'
                                                  )\
        .result()
    assert 'LAX' == cheapest_flights['DestinationLocation']

