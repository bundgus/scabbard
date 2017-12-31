from scabbard import get_client


def test__v1_lists_utilities_views_view_get():
    client = get_client()

    view = client.Utility\
        .V1ListsUtilitiesViewsViewGet(view='BFM_ITIN_TOTAL_PRICE')\
        .result()

    assert 'BFM_ITIN_TOTAL_PRICE' == view['View']['Name']
