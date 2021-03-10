import unittest
from injecta.parameter import placeholder_splitter


class placeholder_splitter_test(unittest.TestCase):  # noqa: N801
    def test_basic(self):
        result = placeholder_splitter.split("foo.bar.hello")

        self.assertEqual(["foo", "bar", "hello"], result)

    def test_quotes_start(self):
        result = placeholder_splitter.split('"bar.me.whatever".hello.foo')

        self.assertEqual(["bar.me.whatever", "hello", "foo"], result)

    def test_quotes_middle(self):
        result = placeholder_splitter.split('foo."bar.me.whatever".hello')

        self.assertEqual(["foo", "bar.me.whatever", "hello"], result)

    def test_quotes_end(self):
        result = placeholder_splitter.split('hello.foo."bar.me.whatever"')

        self.assertEqual(["hello", "foo", "bar.me.whatever"], result)


if __name__ == "__main__":
    unittest.main()
