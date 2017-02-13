from unittest import TestLoader, TestSuite
from .test_sizeparse import SizeParseTestCase

def get_suite():
	# type: () -> TestSuite
	all_tests = TestSuite()
	all_tests.addTest(TestLoader().loadTestsFromTestCase(SizeParseTestCase))
	return all_tests
