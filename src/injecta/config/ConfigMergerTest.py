import unittest
from injecta.config.ConfigMerger import ConfigMerger

class ConfigMergerTest(unittest.TestCase):

    def setUp(self):
        self.__configMerger = ConfigMerger()

    def test_basic(self):
        a = {
            'hello': {
                'world': 1,
                'street': 'Washingtonova',
            },
        }

        b = {
            'hello': {
                'zip': '11000',
            },
        }

        result = self.__configMerger.merge(a, b)

        self.assertEqual({
            'hello': {
                'world': 1,
                'street': 'Washingtonova',
                'zip': '11000',
            }
        }, result)

    def test_overwrite(self):
        a = {
            'hello': {
                'world': 1,
                'street': 'Washingtonova',
            },
        }

        b = {
            'hello': {
                'street': 'Nova',
                'zip': '11000',
            },
        }

        result = self.__configMerger.merge(a, b)

        self.assertEqual({
            'hello': {
                'world': 1,
                'street': 'Nova',
                'zip': '11000',
            }
        }, result)

if __name__ == '__main__':
    unittest.main()
