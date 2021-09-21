import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class SearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Albert\OneDrive\Platzi\Data_courses\Selenium_wt_python\bin\chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")

    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element_by_name("q")
        search_field.clear()

        search_field.send_keys("tee")
        search_field.submit()
        driver.implicitly_wait(15)

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element_by_name("q")

        search_field.send_keys("salt shaker")
        search_field.submit()
        
        products = driver.find_elements_by_xpath('//*[@id="product-collection-image-389"]')
        self.assertEqual(1, len(products))
        driver.implicitly_wait(15)

    def tearDown(self):
        self.driver.quit()
        

if __name__ == "__main__":
    unittest.main(verbosity=2)