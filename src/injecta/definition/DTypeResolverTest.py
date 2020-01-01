import unittest
from injecta.dtype.DType import DType
from injecta.definition.DTypeResolver import DTypeResolver

class DTypeResolverTest(unittest.TestCase):

    def setUp(self):
        self.__typeResolver = DTypeResolver()

    def test_basic(self):
        result = self.__typeResolver.resolve('injecta.bundle.BundleManager')

        self.assertEqual(DType('injecta.bundle.BundleManager', 'BundleManager'), result)

    def test_classic(self):
        result = self.__typeResolver.resolve('importlib.util.LazyLoader')

        self.assertEqual(DType('importlib.util', 'LazyLoader'), result)

if __name__ == '__main__':
    unittest.main()
