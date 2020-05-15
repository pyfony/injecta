import os
import unittest
from injecta.config.YamlConfigReader import YamlConfigReader
from injecta.container.ContainerBuilder import ContainerBuilder
from injecta.container.ContainerInitializer import ContainerInitializer
from injecta.mocks.Foo import Foo
from injecta.mocks.Bar import Bar

class ContainerInitializerTest(unittest.TestCase):

    def setUp(self):
        self.__containerBuilder = ContainerBuilder()

    def test_basic(self):
        baseDir = os.path.dirname(os.path.abspath(__file__))
        config = YamlConfigReader().read(baseDir + '/ContainerInitializerTest_config.yaml')

        containerBuild = ContainerBuilder().build(config)

        container = ContainerInitializer().init(containerBuild)

        foo = container.get(Foo)
        bar = container.get('injecta.mocks.Bar')

        self.assertIsInstance(foo, Foo)
        self.assertIsInstance(bar, Bar)

if __name__ == '__main__':
    unittest.main()
