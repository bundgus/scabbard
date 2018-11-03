# Bargain Finder Max (BFM)
from scabbard import get_client
import json
import datetime
import time


def call_bfm(origin, destination, departure1_datetime, departure2_datetime, mode='live', limit=50, offset=1):
    client = get_client()

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
                                 "LocationCode": "''' + origin + '''"
                             },
                                "DestinationLocation": {
                                    "LocationCode": "''' + destination + '''"
                             }
                         },
                            {
                               "DepartureDateTime": "''' + departure2_datetime + '''",
                               "OriginLocation": {
                                 "LocationCode": "''' + destination + '''"
                             },
                                "DestinationLocation": {
                                    "LocationCode": "''' + origin + '''"
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


def iterate_requests():
    od_pairs = ('HNL-LAX', 'LAX-OGG', 'HNL-BOS', 'HNL-TYO', 'HNL-HND', 'HNL-NRT', 'HNL-SYD',
                'LAX-HNL', 'OGG-LAX', 'BOS-HNL', 'TYO-HNL', 'HND-HNL', 'NRT-HNL', 'SYD-HNL')

    today = datetime.datetime.now()
    departure1_datetime = (today + datetime.timedelta(days=10)).strftime("%Y-%m-%dT%H:%M:%S")
    departure2_datetime = (today + datetime.timedelta(days=11)).strftime("%Y-%m-%dT%H:%M:%S")

    print('departure1_datetime', departure1_datetime)
    print('departure2_datetime', departure2_datetime)

    for i in range(10):
        print('iteration:', i)
        for od in od_pairs:

            for attempt in range(10):
                try:
                    print(od[0:3], od[4:7])
                    itins = call_bfm(od[0:3], od[4:7], departure1_datetime, departure2_datetime)  # , limit=1
                    #print(print(json.dumps(itins)))  # , indent=4
                    time.sleep(30)
                except Exception as e:
                    print(e)
                    print('retrying')
                    time.sleep(30)
                else:
                    break
            else:
                print('failed 10 times, skipping')

    print('departure1_datetime', departure1_datetime)
    print('departure2_datetime', departure2_datetime)


if __name__ == "__main__":
    iterate_requests()
