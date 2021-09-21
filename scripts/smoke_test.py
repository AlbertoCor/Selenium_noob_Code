from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionTest
from search_test import SearchTest


assertions_test = TestLoader().loadTestsFromTestCase(AssertionTest)
searchs_test = TestLoader().loadTestsFromTestCase(SearchTest)

smoke_test = TestSuite([assertions_test, searchs_test])

kwargs = {
    "Salida": "reporte-humo"
}

runner = HTMLTestRunner(kwargs)
runner.run(smoke_test)