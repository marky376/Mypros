#!/usr/bin/env python3

import pytest
from unittest.mock import patch

@pytest.mark.parametrize("city, mock_response, expected", [
    ("London", {"current": {"temp_c": 15}}, {"current": {"temp_c":15}}),
    ("New York", {"current": {"temp_c": 20}}, {"current": {"temp_c": 20}}),
    ("InvalidCity", None, None)
])

def test_get_weather(city, mock_response, expected):
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200 if mock_response else 404
        mock_get.return_value.json.return_value = mock_response
        assert get_weather(city) == expected

