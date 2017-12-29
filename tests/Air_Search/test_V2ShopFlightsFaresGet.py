from scabbard import get_client


def test_v2_shop_flights_fares_get():
    client = get_client()

    fares = client.Air_Search\
        .V2ShopFlightsFaresGet(origin='JFK',
                               destination='LAX',
                               lengthofstay='5',
                               )\
        .result()
    assert 'USD' == fares['FareInfo'][0]['CurrencyCode']
