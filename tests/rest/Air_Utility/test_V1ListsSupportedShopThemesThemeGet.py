from scabbard import get_client


def test__v1_lists_supported_shop_themes_theme_get():
    client = get_client()

    travel_theme = \
        client.Air_Utility\
        .V1ListsSupportedShopThemesThemeGet(theme='BEACH')\
        .result()
    assert 'AAL' == travel_theme['Destinations'][0]['Destination']
