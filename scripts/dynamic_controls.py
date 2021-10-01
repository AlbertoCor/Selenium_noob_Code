import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DynamicControls(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r"C:\Users\Alberto\OneDrive\Platzi\Data_courses\Selenium_wt_python\bin\chromedriver.exe")
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        driver.find_element_by_link_text('Dynamic Controls').click()
        
    def test_name_elements(self):
        driver = self.driver

        checkbox = driver.find_element_by_xpath('//*[@id="checkbox"]/input')
        checkbox.click()

        remove_add_button = driver.find_element_by_css_selector('#checkbox-example > button')
        remove_add_button.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox-example > button')))
        remove_add_button.click()        

        enable_disable_buttom = driver.find_element_by_css_selector('#input-example > button')
        enable_disable_buttom.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#input-example > button')))

        text_area = driver.find_element_by_css_selector('#input-example > input[type=text]')
        text_area.send_keys('Platzi')

        enable_disable_buttom.click()


    def tearDown(self):
        driver = self.driver
        driver.implicitly_wait(3)
        driver.close()
        

if __name__ == "__main__":
    unittest.main(verbosity=2)