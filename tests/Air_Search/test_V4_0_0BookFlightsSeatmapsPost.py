from scabbard import get_client
import json


def test__v4_0_0_book_flights_seatmaps_post():
    client = get_client()

    j = json.loads('''{
              "EnhancedSeatMapRQ": {
                "SeatMapQueryEnhanced": {
                  "RequestType": "Payload",
                  "Flight": {
                    "destination": "EZE",
                    "origin": "DFW",
                  "DepartureDate": {
                    "content": "2018-04-07"
                  },
                  "ArrivalDate": {
                    "content": "2018-04-08"
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
