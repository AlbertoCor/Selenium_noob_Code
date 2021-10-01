import unittest
from selenium import webdriver
from google_page import GooglePage

class GoogleTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path = r"C:\Users\Alberto\OneDrive\Platzi\Data_courses\Selenium_wt_python\bin\chromedriver.exe")

    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('platzi')

        self.assertEqual('platzi', google.keyword)


    @classmethod
    def tearDown(cls):
        cls.driver.close()
        

if __name__ == "__main__":
    unittest.main(verbosity = 0)