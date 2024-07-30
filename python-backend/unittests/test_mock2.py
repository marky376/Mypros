import unittest
from unittest.mock import Mock, patch
from mock_example import get_value_from_dict

class TestMockExample(unittest.TestCase):

    @patch('mock_example.get_value_from_dict')
    def test_get_value_from_dict(self, mock_get_value):
        # Arrange
        mock_dict = {'foo': 'bar'}
        mock_get_value.side_effect = lambda d, k: d[k]
        
        # Act
        result = get_value_from_dict(mock_dict, 'foo')
        
        # Assert
        self.assertEqual(result, 'bar')

if __name__ == '__main__':
    unittest.main()

