from scabbard import get_client


def test__v1_shop_flights_get():
    client = get_client()

    itineraries = client.Air_Search\
        .V1ShopFlightsGet(origin='JFK',
                          destination='LAX',
                          departuredate='2018-04-07',
                          returndate='2018-04-08',
                          eticketsonly='N',
                          pointofsalecountry='US'
                          )\
        .result()
    assert 'JFK' == itineraries['OriginLocation']
