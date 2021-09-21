import unittest
from selenium import webdriver

class HelloWorld(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r"../bin/chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("webpage")


    def tearDown(self):
        self.driver.implicitly_wait(30)
        self.driver.close()
        

if __name__ == "__main__":
    unittest.main(verbosity=2)