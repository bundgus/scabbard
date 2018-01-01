from scabbard import get_client
import json


def test__v3_4_0_shop_altdates_flights_post():
    client = get_client()

    j = json.loads('''{
                     "OTA_AirLowFareSearchRQ": {
                         "AvailableFlightsOnly": true,
                           "POS": {
                                "Source": [{
                                    "PseudoCityCode":"F9CE",
                                    "RequestorID": {
                                        "Type": "1",
                                      "ID": "1",
                                        "CompanyName": {
                                            "Code": "TN",
                                         "CodeContext": "Context"
                                      }
                                 }
                             }]
                            },
                            "OriginDestinationInformation": [{
                              "DepartureDateTime": "2018-04-07T00:00:00",
                               "OriginLocation": {
                                 "LocationCode": "TLV"
                             },
                                "DestinationLocation": {
                                    "LocationCode": "BCN"
                             },
                                "TPA_Extensions": {
                                 "ConnectionTime": {
                                     "Max": 0
                                    }
                             }
                         },
                            {
                             "DepartureDateTime": "2018-04-08T00:00:00",
                               "OriginLocation": {
                                 "LocationCode": "BCN"
                             },
                                "DestinationLocation": {
                                    "LocationCode": "TLV"
                             },
                                "TPA_Extensions": {
                                 "ConnectionTime": {
                                     "Max": 0
                                    }
                             }
                         }],
                           "TravelPreferences": {
                              "ValidInterlineTicket": true,
                               "TPA_Extensions": {
                                 "InterlineIndicator": {
                                     "Ind": true
                                 }
                             }
                         },
                            "TravelerInfoSummary": {
                                "AirTravelerAvail": [{
                                  "PassengerTypeQuantity": [{
                                     "Code": "ADT",
                                        "Quantity": 1
                                   }]
                                }],
                               "PriceRequestInformation": {
                                    "CurrencyCode": "USD"
                             }
                         },
                            "TPA_Extensions": {
                             "IntelliSellTransaction": {
                                 "RequestType": {
                                        "Name": "AD1"
                                 },
                                    "CompressResponse": {
                                       
                                  }
                             }
                         }
                     }
                    }''')

    itineraries = client.Air_Search\
        .V3_4_0ShopAltdatesFlightsPost(bargainfindermaxalternatedaterequest=j,
                                          mode='live',
                                          limit='50',
                                          offset=1
                                          )\
        .result()
    assert '3.4.0' == itineraries['OTA_AirLowFareSearchRS']['Version']
