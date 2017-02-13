import unittest
import sizeparse

class SizeParseTestCase(unittest.TestCase):
	def _test_parse(self, value, result):
		self.assertEqual(sizeparse.parse(value), result)

	def _test_parse_all_cases(self, number, suffix, result):
		self._test_parse("%d%s" % (number, suffix), result)
		self._test_parse("%d%sb" % (number, suffix), result)
		self._test_parse("%d%s" % (number, suffix.upper()), result)
		self._test_parse("%d%sb" % (number, suffix.upper()), result)
		self._test_parse("%d%sB" % (number, suffix), result)
		self._test_parse("%d%sB" % (number, suffix.upper()), result)
		self._test_parse("%d %s" % (number, suffix), result)
		self._test_parse("%d %sb" % (number, suffix), result)
		self._test_parse("%d %s" % (number, suffix.upper()), result)
		self._test_parse("%d %sb" % (number, suffix.upper()), result)
		self._test_parse("%d %sB" % (number, suffix), result)
		self._test_parse("%d %sB" % (number, suffix.upper()), result)

	def _test_not_parse(self, value):
		with self.assertRaises(sizeparse.SizeParseError):
			sizeparse.parse(value)

	def test_valid_values(self):
		self._test_parse_all_cases(1, "", 1)
		self._test_parse_all_cases(10, "", 10)
		self._test_parse_all_cases(1, "k", 1000)
		self._test_parse_all_cases(10, "k", 10000)
		self._test_parse_all_cases(10, "ki", 10240)
		self._test_parse_all_cases(10, "mi", 10485760)

	def test_invalid_values(self):
		self._test_not_parse("1a")
		self._test_not_parse("1ab")
		self._test_not_parse("1kbi")
		self._test_not_parse("1ikb")
		self._test_not_parse("kb1")
		self._test_not_parse("1kmb")
