import unittest
from injecta.container.ContainerBuild import ContainerBuild
from injecta.dtype.DType import DType
from injecta.service.Service import Service
from injecta.service.argument.ListArgument import ListArgument
from injecta.service.argument.PrimitiveArgument import PrimitiveArgument
from injecta.service.argument.TaggedServicesArgument import TaggedServicesArgument
from injecta.service.class_.InspectedArgument import InspectedArgument
from injecta.service.resolved.ResolvedArgument import ResolvedArgument
from injecta.tag.TaggedArgumentResolver import TaggedArgumentResolver

class TaggedArgumentResolverTest(unittest.TestCase):

    def setUp(self):
        self.__taggedArgumentResolver = TaggedArgumentResolver()

    def test_noChange(self):
        resolvedArgument = ResolvedArgument(
            'myNumber',
            PrimitiveArgument(123),
            InspectedArgument('myNumber', DType('builtins', 'int'))
        )
        containerBuild = ContainerBuild({}, [], {}, {}, {})

        newResolvedArgument = self.__taggedArgumentResolver.resolve(resolvedArgument, containerBuild)

        self.assertEqual(resolvedArgument, newResolvedArgument)

    def test_basic(self):
        resolvedArgument = ResolvedArgument(
            'myNumber',
            TaggedServicesArgument('myServiceTag'),
            InspectedArgument('myTaggedServices', DType('builtins', 'list'))
        )

        newResolvedArgument = self.__taggedArgumentResolver.resolve(resolvedArgument, self.__createContainerBuild())

        listArgument = newResolvedArgument.argument

        self.assertIsInstance(listArgument, ListArgument)
        self.assertEqual(None, listArgument.name)
        self.assertEqual('injecta.mocks.Bar', listArgument.items[0].serviceName)
        self.assertEqual('injecta.mocks.Bar.new', listArgument.items[1].serviceName)

    def test_namedArgument(self):
        resolvedArgument = ResolvedArgument(
            'myNumber',
            TaggedServicesArgument('myServiceTag', 'myTaggedServices'),
            InspectedArgument('myTaggedServices', DType('builtins', 'list'))
        )

        newResolvedArgument = self.__taggedArgumentResolver.resolve(resolvedArgument, self.__createContainerBuild())

        listArgument = newResolvedArgument.argument

        self.assertIsInstance(listArgument, ListArgument)
        self.assertEqual('myTaggedServices', listArgument.name)
        self.assertEqual('injecta.mocks.Bar', listArgument.items[0].serviceName)
        self.assertEqual('injecta.mocks.Bar.new', listArgument.items[1].serviceName)

    def __createContainerBuild(self):
        tags2Services = {
            'myServiceTag': [
                Service('injecta.mocks.Bar', DType('injecta.mocks.Bar', 'Bar')),
                Service('injecta.mocks.Bar.new', DType('injecta.mocks.Bar', 'Bar'))
            ]
        }

        return ContainerBuild({}, [], {}, {}, tags2Services)

if __name__ == '__main__':
    unittest.main()
