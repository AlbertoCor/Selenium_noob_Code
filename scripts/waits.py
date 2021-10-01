import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By             # support reference to a website for interact different from driver
from selenium.webdriver.support.ui import WebDriverWait     # use expected condition and explicit waits make available
from selenium.webdriver.support import expected_conditions as EC 

class ExplicitWaitTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r"C:\Users\Alberto\OneDrive\Platzi\Data_courses\Selenium_wt_python\bin\chromedriver.exe")
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")


    def test_account_link(self):
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_id('select-language').get_attribute('length') == '3')

        account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
        account.click()

    def test_create_new_customer(self):
        driver = self.driver
        driver.find_element_by_link_text('ACCOUNT').click()

        my_account = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "My Account")))
        my_account.click()

        create_account_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "CREATE AN ACCOUNT")))
        create_account_button.click()

        WebDriverWait(driver, 10).until(EC.title_contains('Create New Customer Account'))

    def tearDown(self):
        self.driver.close()
        

if __name__ == "__main__":
    unittest.main(verbosity=2)