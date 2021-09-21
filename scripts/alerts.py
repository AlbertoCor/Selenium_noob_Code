import unittest
from selenium import webdriver

class CompareProducts(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r"C:\Users\Alberto\OneDrive\Platzi\Data_courses\Selenium_wt_python\bin\chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")

    def test_compare_products_removal_alerts(self):
        driver = self.driver
        serach_field = driver.find_element_by_name('q')
        serach_field.clear()

        serach_field.send_keys('tee')
        serach_field.submit()

        driver.find_element_by_class_name('link-compare').click()
        driver.find_element_by_link_text('Clear All').click()

        # here we catch the alert type and automate the actions
        alert = driver.switch_to_alert()
        alert_text = alert.text

        # verify message of alert to ensure we automate well
        self.assertEqual("Are you sure you would like to remove all products from your comparison?", alert_text)

        # add the actions to do in that alert
        alert.accept()

    def tearDown(self):
        self.driver.implicitly_wait(30)
        self.driver.close()
        

if __name__ == "__main__":
    unittest.main(verbosity=2)