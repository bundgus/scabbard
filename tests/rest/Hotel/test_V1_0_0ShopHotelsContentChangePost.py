from scabbard import get_client
import json
import datetime


def test__v1_0_0_shop_hotels_content_change_post():
    client = get_client()

    today = datetime.datetime.now()
    start_date = (today + datetime.timedelta(days=10)).strftime("%Y-%m-%d")
    end_date = (today + datetime.timedelta(days=11)).strftime("%Y-%m-%d")

    j = json.loads('''{

                      "GetHotelContentChangeRQ": {
                    
                        "ContentChangeRef": {
                    
                          "StartDate": "''' + start_date + '''",
                    
                          "EndDate": "''' + end_date + '''"
                    
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
