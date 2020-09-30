import unittest
from injecta.parameter.placeholderReplacer import replacePlaceholder

class placeholderReplacerTest(unittest.TestCase):

    def test_string(self):
        result = replacePlaceholder('hello %name%', 'name', 'Jiri', 'company.owner')

        self.assertEqual('hello Jiri', result)

    def test_intSolo(self):
        result = replacePlaceholder('%houseNumber%', 'houseNumber', 3901, 'company.address')

        self.assertEqual(3901, result)

    def test_intConcat(self):
        result = replacePlaceholder('House number: %houseNumber%', 'houseNumber', 3901, 'company.address')

        self.assertEqual('House number: 3901', result)

    def test_listSolo(self):
        result = replacePlaceholder('%emails%', 'emails', ['me@me.com', 'johny@example.com'], 'job.onErrorNotifications')

        self.assertEqual(['me@me.com', 'johny@example.com'], result)

    def test_listConcat(self):
        with self.assertRaises(Exception) as error:
            replacePlaceholder('Emails: %emails%', 'emails', ['me@me.com', 'johny@example.com'], 'job.onErrorNotifications')

        self.assertEqual('Merging list parameters with other variable types is not allowed in job.onErrorNotifications', str(error.exception))

    def test_noneSolo(self):
        result = replacePlaceholder('%instanceType%', 'instanceType', None, 'job.clusterInstance')

        self.assertEqual(None, result)

    def test_noneConcat(self):
        with self.assertRaises(Exception) as error:
            replacePlaceholder('Instance type: %instanceType%', 'instanceType', None, 'job.clusterInstance')

        self.assertEqual('Merging None value with other variable types is not allowed in job.clusterInstance', str(error.exception))

if __name__ == '__main__':
    unittest.main()
