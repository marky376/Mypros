import unittest
from unittest.mock import patch, Mock
from utils import get_json


class TestGetJson(unittest.TestCase):
    @patch('utils.requests.get')
    def test_get_json(self, mock_get):
        # Arrange
        mock_response = Mock()
        expected_json = {'key': 'value'}
        mock_response.json.return_value = expected_json
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Act
        url = 'https://api.github.com'
        result = get_json(url)

        # Assert
        self.assertEqual(result, expected_json)
        mock_get.assert_called_once_with(url, timeout=5)
        mock_response.raise_for_status.assert_called_once()



if __name__ == '__main__':
    unittest.main()
