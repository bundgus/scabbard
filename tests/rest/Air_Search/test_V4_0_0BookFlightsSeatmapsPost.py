from scabbard import get_client
import json
import datetime


def test__v4_0_0_book_flights_seatmaps_post():
    client = get_client()

    today = datetime.datetime.now()
    departure_date = (today + datetime.timedelta(days=10)).strftime("%Y-%m-%d")
    arrival_date = (today + datetime.timedelta(days=10)).strftime("%Y-%m-%d")


    j = json.loads('''{
              "EnhancedSeatMapRQ": {
                "SeatMapQueryEnhanced": {
                  "RequestType": "Payload",
                  "Flight": {
                    "destination": "EZE",
                    "origin": "DFW",
                  "DepartureDate": {
                    "content": "''' + departure_date + '''"
                  },
                  "ArrivalDate": {
                    "content": "''' + arrival_date + '''"
                  },
                  "Operating": {
                    "carrier": "AA",
                    "content": "997"
                  },
                  "Marketing": [{
                    "carrier": "AA",
                    "content": "997"
                  }]
                  }
                }
              }
            }''')

    seat_map = client.Air_Search\
        .V4_0_0BookFlightsSeatmapsPost(seatmaprequest=j,
                                       mode='seatmaps'
                                       )\
        .result()
    assert 'Complete' == seat_map['EnhancedSeatMapRS']['ApplicationResults']['status']
