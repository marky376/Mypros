#!/usr/bin/env python3
from unittest.mock import MagicMock
from unittest.mock import Mock
# configuring magicmock to specify retun values or limit attributes that are aavailable
#thing = ProductionClass()
#thing.method = MagicMock(return_value=3)
#thing.method(3, 4, 5, key='value')
#3
#thing.method.assert_called_with(3, 4, 5, key='value')

mock = Mock(side_effect=KeyError('foo'))
mock()
