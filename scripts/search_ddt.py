import unittest
from ddt import ddt, data, unpack
from selenium import webdriver


@ddt
class SearchDDT(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r"C:\Users\Alberto\OneDrive\Platzi\Data_courses\Selenium_wt_python\bin\chromedriver.exe")
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")

    # use decorator with specified data of input to object built
    @data(('dress', 5), ('music', 5))
    # with unpack, take value from tuple of data and use on object
    @unpack

    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver

        # sequence in webpage automated
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        # count products quantity, show it name product and compare with our qty vs webpage qty
        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')
        print(f'found {len(products)} products')

        for product in products:
            print(product.text)

        self.assertEqual(expected_count, len(products))

    def tearDown(self):
        self.driver.close()
        

if __name__ == "__main__":
    unittest.main()