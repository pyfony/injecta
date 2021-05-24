import unittest
from injecta.dtype import fullname
from injecta.mocks.Bar import Bar


class FullnameTest(unittest.TestCase):
    def test_object(self):
        result = fullname.get(Bar("Hello"))

        self.assertEqual("injecta.mocks.Bar.Bar", result)

    def test_class(self):
        result = fullname.get(Bar)

        self.assertEqual("injecta.mocks.Bar.Bar", result)

    def test_builtin(self):
        result = fullname.get(str)

        self.assertEqual("str", result)


if __name__ == "__main__":
    unittest.main()
