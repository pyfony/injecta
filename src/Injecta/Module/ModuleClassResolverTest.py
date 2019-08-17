import unittest
from Injecta.Module.ModuleClassResolver import ModuleClassResolver

class ModuleClassResolverTest(unittest.TestCase):

    def setUp(self):
        self.__moduleClassResolver = ModuleClassResolver()

    def test_standard(self):
        moduleClass = self.__moduleClassResolver.resolve('importlib.util.LazyLoder')

        self.assertEqual('importlib.util', moduleClass.getModuleName())
        self.assertEqual('LazyLoder', moduleClass.getClassName())

    def test_classNameInModuleName(self):
        moduleClass = self.__moduleClassResolver.resolve('Injecta.Service.Definition')

        self.assertEqual('Injecta.Service.Definition', moduleClass.getModuleName())
        self.assertEqual('Definition', moduleClass.getClassName())

if __name__ == '__main__':
    unittest.main()
