import unittest
from selenium import webdriver
from time import sleep

class NavTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r"C:\Users\Alberto\OneDrive\Platzi\Data_courses\Selenium_wt_python\bin\chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://www.google.com/")

    def test_browser_nav(self):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('platzi') # send to search bar string text
        search_field.submit()

        # add time make execution longer to finish
        driver.back()   # back 1 page and refresh 
        sleep(3)
        driver.forward()
        sleep(3)
        driver.refresh()
        sleep(3)


    def tearDown(self):
        self.driver.implicitly_wait(30)
        self.driver.close()
        

if __name__ == "__main__":
    unittest.main(verbosity=2)