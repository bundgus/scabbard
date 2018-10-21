from scabbard import get_client
import json
import datetime


def test__v3_4_0_shop_altairports_flights_post():
    client = get_client()

    today = datetime.datetime.now()
    departure1_datetime = (today + datetime.timedelta(days=10)).strftime("%Y-%m-%dT%H:%M:%S")
    departure2_datetime = (today + datetime.timedelta(days=11)).strftime("%Y-%m-%dT%H:%M:%S")

    j = json.loads('''{
                      "OTA_AirLowFareSearchRQ": {
                        "OriginDestinationInformation": [
                          {
                            "DepartureDateTime": "''' + departure1_datetime + '''",
                            "DestinationLocation": {
                              "LocationCode": "LAX"
                            },
                            "OriginLocation": {
                              "LocationCode": "DFW"
                            },
                            "RPH": "1"
                          },
                          {
                            "DepartureDateTime": "''' + departure2_datetime + '''",
                            "DestinationLocation": {
                              "LocationCode": "DFW"
                            },
                            "OriginLocation": {
                              "LocationCode": "LAX"
                            },
                            "RPH": "2"
                          }
                        ],
                        "POS": {
                          "Source": [
                            {
                              "PseudoCityCode":"F9CE",
                              "RequestorID": {
                                "CompanyName": {
                                  "Code": "TN"
                                },
                                "ID": "REQ.ID",
                                "Type": "0.AAA.X"
                              }
                            }
                          ]
                        },
                        "TPA_Extensions": {
                          "IntelliSellTransaction": {
                            "RequestType": {
                              "Name": "50ITINS"
                            }
                          }
                        },
                        "TravelerInfoSummary": {
                          "AirTravelerAvail": [
                            {
                              "PassengerTypeQuantity": [
                                {
                                  "Code": "ADT",
                                  "Quantity": 1
                                }
                              ]
                            }
                          ]
                        }
                      }
                    }''')

    itineraries = client.Air_Search\
        .V3_4_0ShopAltairportsFlightsPost(bargainfindermaxalternateairportrequest=j,
                                          mode='live',
                                          limit='50',
                                          offset=1
                                          )\
        .result()
    assert '3.4.0' == itineraries['OTA_AirLowFareSearchRS']['Version']
