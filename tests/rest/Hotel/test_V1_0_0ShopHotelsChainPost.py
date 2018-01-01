from scabbard import get_client
import json


def test__v1_0_0_shop_hotels_chain_post():
    client = get_client()

    j = json.loads('''{"GetHotelChainInfoRQ": {}}''')

    hotel_chains = client.Hotel\
        .V1_0_0ShopHotelsChainPost(gethotelchaininforequest=j,
                                   mode='chain'
                                   )\
        .result()
    assert 29 == len(hotel_chains['GetHotelChainInfoRS']['ApplicationResults']
                     ['Success'][0]['timeStamp'])
