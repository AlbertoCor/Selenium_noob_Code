import unittest
from selenium import webdriver

class Typos(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r"C:\Users\Alberto\OneDrive\Platzi\Data_courses\Selenium_wt_python\bin\chromedriver.exe")
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        driver.find_element_by_link_text('Typos').click()


    def test_find_typo(self):
        driver = self.driver

        paragraphToCheck = driver.find_element_by_css_selector('#content > div > p:nth-child(3)')
        text_to_check = paragraphToCheck.text
        print(text_to_check)

        tries = 1 # number of tries to find correct
        found = False

        correct_text = "Sometimes you'll see a typo, other times you won't."

        while text_to_check != correct_text:
            paragraphToCheck = driver.find_element_by_css_selector('#content > div > p:nth-child(3)')
            text_to_check = paragraphToCheck.text  
            driver.refresh()

        while not found:
            if text_to_check == correct_text:
                tries += 1
                driver.refresh()
                found = True

        self.assertEqual(found, True)

        print(f'Took {tries} refresh to correct typo')

if __name__ == "__main__":
    unittest.main(verbosity=2)