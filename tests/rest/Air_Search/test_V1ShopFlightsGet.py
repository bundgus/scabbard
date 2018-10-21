from scabbard import get_client
import datetime

def test__v1_shop_flights_get():
    client = get_client()

    today = datetime.datetime.now()
    departure_date = (today + datetime.timedelta(days=10)).strftime("%Y-%m-%d")
    return_date = (today + datetime.timedelta(days=11)).strftime("%Y-%m-%d")

    itineraries = client.Air_Search\
        .V1ShopFlightsGet(origin='JFK',
                          destination='LAX',
                          departuredate=departure_date,
                          returndate=return_date,
                          eticketsonly='N',
                          pointofsalecountry='US'
                          )\
        .result()
    assert 'JFK' == itineraries['OriginLocation']
