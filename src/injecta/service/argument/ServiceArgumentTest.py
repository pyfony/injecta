import unittest
from injecta.dtype.DType import DType
from injecta.service.argument.ServiceArgument import ServiceArgument
from injecta.service.class_.InspectedArgument import InspectedArgument

class ServiceArgumentTest(unittest.TestCase):

    def test_basic(self):
        serviceArgument = ServiceArgument('foo.Bar')
        inspectedArgument = InspectedArgument('bar', DType('foo.Bar', 'Bar'))
        services2Classes = {'foo.Bar': DType('foo.Bar', 'Bar')}

        serviceArgument.checkTypeMatchesDefinition(inspectedArgument, services2Classes)

    def test_undefinedService(self):
        serviceArgument = ServiceArgument('foo.Bar')
        inspectedArgument = InspectedArgument('bar', DType('foo.Bar', 'Bar'))
        services2Classes = {}

        with self.assertRaises(Exception) as error:
            serviceArgument.checkTypeMatchesDefinition(inspectedArgument, services2Classes)

        self.assertEqual('Undefined service foo.Bar', str(error.exception))

    def test_interface(self):
        serviceArgument = ServiceArgument('injecta.mocks.Bar')
        inspectedArgument = InspectedArgument('bar', DType('injecta.mocks.BarInterface', 'BarInterface'))
        services2Classes = {'injecta.mocks.Bar': DType('injecta.mocks.Bar', 'Bar')}

        serviceArgument.checkTypeMatchesDefinition(inspectedArgument, services2Classes)

if __name__ == '__main__':
    unittest.main()
