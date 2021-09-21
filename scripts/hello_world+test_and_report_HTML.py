import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = r"C:/Users/Albert/OneDrive/Platzi/Data_courses/Selenium_wt_python/bin/chromedriver.exe")
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello_world(self):
        driver = self.driver
        driver.get("https://www.platzi.com")
        driver.implicitly_wait(10)

    def test_visit_wiki(self):
        driver = self.driver
        driver.get("https://www.wikipedia.org")
        driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner= HTMLTestRunner(output = "report", report_name = "hello_world-report"))