from scabbard import get_client
import json


def test__v1_0_0_shop_hotels_content_change_post():
    client = get_client()

    j = json.loads('''{

                      "GetHotelContentChangeRQ": {
                    
                        "ContentChangeRef": {
                    
                          "StartDate": "2015-05-18",
                    
                          "EndDate": "2015-05-23"
                    
                        }
                    
                      }
                    
                    }''')

    change = client.Hotel\
        .V1_0_0ShopHotelsContentChangePost(gethotelcontentchangerequest=j,
                                           mode='change'
                                           )\
        .result()

    assert 29 == len(change['GetHotelContentChangeRS']['ApplicationResults']
                     ['Success'][0]['timeStamp'])
