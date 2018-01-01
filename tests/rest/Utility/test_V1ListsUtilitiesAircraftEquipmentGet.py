from scabbard import get_client


def test__v1_lists_utilities_aircraft_equipment_get():
    client = get_client()

    equipment = client.Utility\
        .V1ListsUtilitiesAircraftEquipmentGet(aircraftcode='M80')\
        .result()
    assert 'M80' == equipment['AircraftInfo'][0]['AircraftCode']
