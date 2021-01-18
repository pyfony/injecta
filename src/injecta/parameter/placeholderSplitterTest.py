import unittest
from injecta.parameter import placeholderSplitter

class placeholderSplitterTest(unittest.TestCase):

    def test_basic(self):
        result = placeholderSplitter.split('foo.bar.hello')

        self.assertEqual(['foo', 'bar', 'hello'], result)

    def test_quotesStart(self):
        result = placeholderSplitter.split('"bar.me.whatever".hello.foo')

        self.assertEqual(['bar.me.whatever', 'hello', 'foo'], result)

    def test_quotesMiddle(self):
        result = placeholderSplitter.split('foo."bar.me.whatever".hello')

        self.assertEqual(['foo', 'bar.me.whatever', 'hello'], result)

    def test_quotesEnd(self):
        result = placeholderSplitter.split('hello.foo."bar.me.whatever"')

        self.assertEqual(['hello', 'foo', 'bar.me.whatever'], result)

if __name__ == '__main__':
    unittest.main()
