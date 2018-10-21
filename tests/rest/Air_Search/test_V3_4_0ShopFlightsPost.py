from scabbard import get_client
import json
import datetime


def test__v3_4_0_shop_flights_post():
    client = get_client()

    today = datetime.datetime.now()
    departure1_datetime = (today + datetime.timedelta(days=10)).strftime("%Y-%m-%dT%H:%M:%S")
    departure2_datetime = (today + datetime.timedelta(days=11)).strftime("%Y-%m-%dT%H:%M:%S")

    j = json.loads('''{
                     "OTA_AirLowFareSearchRQ": {
                         "Target": "Production",
                           "POS": {
                                "Source": [{
                                    "PseudoCityCode":"F9CE",
                                    "RequestorID": {
                                        "Type": "1",
                                      "ID": "1",
                                        "CompanyName": {
                                            
                                      }
                                 }
                             }]
                            },
                            "OriginDestinationInformation": [{
                              "RPH": "1",
                               "DepartureDateTime": "''' + departure1_datetime + '''",
                               "OriginLocation": {
                                 "LocationCode": "DFW"
                             },
                                "DestinationLocation": {
                                    "LocationCode": "CDG"
                             },
                                "TPA_Extensions": {
                                 "SegmentType": {
                                        "Code": "O"
                                   }
                             }
                         },
                            {
                             "RPH": "2",
                               "DepartureDateTime": "''' + departure2_datetime + '''",
                               "OriginLocation": {
                                 "LocationCode": "CDG"
                             },
                                "DestinationLocation": {
                                    "LocationCode": "DFW"
                             },
                                "TPA_Extensions": {
                                 "SegmentType": {
                                        "Code": "O"
                                   }
                             }
                         }],
                           "TravelPreferences": {
                              "ValidInterlineTicket": true,
                               "CabinPref": [{
                                 "Cabin": "Y",
                                 "PreferLevel": "Preferred"
                                }],
                               "TPA_Extensions": {
                                 "TripType": {
                                       "Value": "Return"
                                 },
                                    "LongConnectTime": {
                                        "Min": 780,
                                     "Max": 1200,
                                        "Enable": true
                                  },
                                    "ExcludeCallDirectCarriers": {
                                      "Enabled": true
                                 }
                             }
                         },
                            "TravelerInfoSummary": {
                                "SeatsRequested": [1],
                              "AirTravelerAvail": [{
                                  "PassengerTypeQuantity": [{
                                     "Code": "ADT",
                                        "Quantity": 1
                                   }]
                                }]
                            },
                            "TPA_Extensions": {
                             "IntelliSellTransaction": {
                                 "RequestType": {
                                        "Name": "50ITINS"
                                 }
                             }
                         }
                     }
                    }''')

    itineraries = client.Air_Search\
        .V3_4_0ShopFlightsPost(bargainfindermaxrequest=j,
                                       mode='live',
                                       limit='50',
                                       offset=1
                                       )\
        .result()
    assert '3.4.0' == itineraries['OTA_AirLowFareSearchRS']['Version']
