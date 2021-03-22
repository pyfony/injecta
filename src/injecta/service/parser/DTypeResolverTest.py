import unittest
from injecta.dtype.DType import DType
from injecta.service.parser.DTypeResolver import DTypeResolver


class DTypeResolverTest(unittest.TestCase):
    def setUp(self):
        self.__type_resolver = DTypeResolver()

    def test_basic(self):
        result = self.__type_resolver.resolve("injecta.parameter.ParametersParser")

        self.assertEqual(DType("injecta.parameter.ParametersParser", "ParametersParser"), result)

    def test_classic(self):
        result = self.__type_resolver.resolve("importlib.util.LazyLoader")

        self.assertEqual(DType("importlib.util", "LazyLoader"), result)


if __name__ == "__main__":
    unittest.main()
