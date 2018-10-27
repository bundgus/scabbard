# Bargain Finder Max (BFM)
from scabbard import get_client
import json
import datetime


def call_bfm(mode='live', limit=50, offset=1):
    client = get_client()

    today = datetime.datetime.now()
    departure1_datetime = (today + datetime.timedelta(days=10)).strftime("%Y-%m-%dT%H:%M:%S")
    departure2_datetime = (today + datetime.timedelta(days=11)).strftime("%Y-%m-%dT%H:%M:%S")

    j = json.loads('''{
                     "OTA_AirLowFareSearchRQ": {
                         "POS": {
                                "Source": [{
                                    "PseudoCityCode":"F9CE",
                                    "RequestorID": {
                                        "Type": "1",
                                        "ID": "1"
                                 }
                             }]
                            },
                            "OriginDestinationInformation": [{

                               "DepartureDateTime": "''' + departure1_datetime + '''",
                               "OriginLocation": {
                                 "LocationCode": "DFW"
                             },
                                "DestinationLocation": {
                                    "LocationCode": "IAH"
                             }
                         },
                            {
                               "DepartureDateTime": "''' + departure2_datetime + '''",
                               "OriginLocation": {
                                 "LocationCode": "IAH"
                             },
                                "DestinationLocation": {
                                    "LocationCode": "DFW"
                             }
                         }],
                            "TravelerInfoSummary": {
                                "AirTravelerAvail": [{
                                  "PassengerTypeQuantity": [{
                                     "Code": "ADT",
                                        "Quantity": 1
                                   }]
                                }]
                            }
                     }
                    }''')

    itineraries = client.Air_Search \
        .V4_3_0ShopFlightsPost(bargainfindermaxrequest=j,
                               mode=mode,
                               limit=str(limit),
                               offset=offset
                               ) \
        .result()

    return itineraries


if __name__ == "__main__":
    itins = call_bfm(limit=1)
    print(print(json.dumps(itins, indent=4)))
