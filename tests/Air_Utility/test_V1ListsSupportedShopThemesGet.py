from scabbard import get_client


def test__v1_lists_supported_shop_themes_get():
    client = get_client()

    travel_themes = client.Air_Utility\
        .V1ListsSupportedShopThemesGet().result()
    assert 'BEACH' == travel_themes['Themes'][0]['Theme']
