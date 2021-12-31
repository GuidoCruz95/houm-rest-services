import pytest

from curl_access import curl_functions

test_data = {
    "houmers": [
        {
            "id": 1001,
            "name": "Jose",
            "last_name": "maria cardenas",
            "current_location": "-33.387451296071845, -70.61456199591032"
        }, {
            "id": 1002,
            "name": "Daniela",
            "last_name": "Perez Ovando",
            "current_location": "-33.38896955808164, -70.61746647304639"
        }
    ],
    "places": [
        {
            "id": 2001,
            "owner": "Unknown",
            "name": "Houm office",
            "description": "Main Houm office",
            "location": "-33.387451296071845, -70.61456199591032"
        }
    ],
    "visitors": [
        {
            "id": 3001,
            "name": "Luis",
            "last_name": "Zeballos Mamani",
            "current_location": "-33.387451296071845, -70.61456199591032"
        }
    ]
}


class TestCurlFunctions:

    @pytest.mark.parametrize(
        "function, data, expected",
        [
            (curl_functions.get_houms, {"places": []}, 0),
            (curl_functions.get_houms, test_data, 2),
            (curl_functions.get_houms, {}, 0),

            (curl_functions.get_visitors, {"places": []}, 0),
            (curl_functions.get_visitors, test_data, 1),
            (curl_functions.get_visitors, {}, 0),

            (curl_functions.get_places, {"places": []}, 0),
            (curl_functions.get_places, test_data, 1),
            (curl_functions.get_places, {}, 0),
        ]
    )
    def test_get_items(self, function, data, expected):
        curl_functions.data = data
        assert len(function()) == expected

    @pytest.mark.parametrize(
        "function, data, identifier, expected",
        [
            (curl_functions.get_houm, {"places": []}, 1001, None),
            (
                    curl_functions.get_houm,
                    test_data,
                    1002,
                    {
                        'id': 1002,
                        'name': 'Daniela',
                        'last_name': 'Perez Ovando',
                        'current_location': '-33.38896955808164, -70.61746647304639'
                    }
            ),
            (curl_functions.get_houm, {}, 1001, None),

            (curl_functions.get_place, {"places": []}, 2001, None),
            (
                    curl_functions.get_place,
                    test_data,
                    2001,
                    {
                        "id": 2001,
                        "owner": "Unknown",
                        "name": "Houm office",
                        "description": "Main Houm office",
                        "location": "-33.387451296071845, -70.61456199591032"
                    }
            ),
            (curl_functions.get_place, {}, 2001, None),

            (curl_functions.get_visitor, {"places": []}, 3001, None),
            (
                    curl_functions.get_visitor,
                    test_data,
                    3001,
                    {
                        "id": 3001,
                        "name": "Luis",
                        "last_name": "Zeballos Mamani",
                        "current_location": "-33.387451296071845, -70.61456199591032"
                    }
            ),
            (curl_functions.get_visitor, {}, 3001, None),
        ]
    )
    def test_get_items_by_identifier(self, function, data, identifier, expected):
        curl_functions.data = data
        assert function(identifier) == expected
