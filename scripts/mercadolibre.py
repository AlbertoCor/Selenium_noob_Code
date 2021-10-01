import unittest
from selenium import webdriver, sleep


"""
This program objective is automate search of a ps4 in mercado libre store page

steps: 

1.- Enter mercadolibre.com
2.- Select colombia as country
3.- Search "playstation 4 "
4.- filter by new product
5.- filter by location "Bogota"
6.- Order by higher to lower
7.- Get name and price from 1st to 5 place products
"""

class TestingMercadolibre(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r"C:\Users\Alberto\OneDrive\Platzi\Data_courses\Selenium_wt_python\bin\chromedriver.exe")
        driver = self.driver
        driver.get("https://mercadolibre.com/")
        driver.maximize_window()

    def test_search_ps4(self):
        driver = self.driver

        country = driver.find_element_by_id('CO')
        country.click()

        search_field = driver.find_element_by_name('as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('playstation 4')
        search_field.submit()
        sleep(3)

        location = driver.find_element_by_partial_link_text('Bogotá D.C.')
        location.click()
        sleep(3)

        condition = driver.find_element_by_partial_link_text('Nuevo')
        condition.click()
        sleep(3)

        




    def tearDown(self):
        self.driver.close()
        

if __name__ == "__main__":
    unittest.main(verbosity=0)