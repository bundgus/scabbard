from scabbard import get_client
import json


def test__v3_4_0_shop_altairports_flights_post():
    client = get_client()

    j = json.loads('''{
                      "OTA_AirLowFareSearchRQ": {
                        "OriginDestinationInformation": [
                          {
                            "DepartureDateTime": "2018-04-07T00:00:00",
                            "DestinationLocation": {
                              "LocationCode": "LAX"
                            },
                            "OriginLocation": {
                              "LocationCode": "DFW"
                            },
                            "RPH": "1"
                          },
                          {
                            "DepartureDateTime": "2018-04-08T00:00:00",
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
