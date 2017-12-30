from scabbard import get_client


def test_v2_shop_flights_fares_get():
    client = get_client()

    fares = client.Air_Search\
        .V2ShopFlightsFaresGet(origin='JFK',
                               destination='LAX',
                               lengthofstay='5',
                               pointofsalecountry='US'
                               )\
        .result()
    assert 1 <= len(fares['FareInfo'][0]['CurrencyCode'])
    print()
    # must implement logic to handle inconsistent return data schema
    for c in fares['FareInfo']:
        if isinstance(c['LowestNonStopFare'], dict):
            for ac in c['LowestNonStopFare']['AirlineCodes']:
                print(ac)
            print(c['LowestNonStopFare']['Fare'])
        elif isinstance(c['LowestNonStopFare'], str):  # if value is 'N/A'
            print(c['LowestNonStopFare'])
