import unittest
from selenium import webdriver
from time import sleep

class HelloWorld(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r"C:\Users\Alberto\OneDrive\Platzi\Data_courses\Selenium_wt_python\bin\chromedriver.exe")
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
        # driver.find_element_by_link_text('Add/Remove Elements').click()
        
    def test_add_remove(self):
        driver = self.driver

        elements_added = int(input("how many elementswill you add?: "))
        elements_removed = int(input("How many elements will you remove? "))
        total_elements = elements_added - elements_removed

        add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button')

        sleep(3)

        for i in range (elements_added):
            add_button.click()
        sleep(2)
        for j in range (elements_removed):
            try:
                delete_button = driver.find_element_by_xpath('//*[@id="elements"]/button[1]')
                delete_button.click()
            except:
                print("you trying to delete more elements that exist")
                break
        sleep(2)
        if total_elements > 0:
            print(f"There are {total_elements} elements on screen")
        else:
            print('there are 0 elements on screen')

        sleep(2)


    def tearDown(self):
        self.driver.close()
        

if __name__ == "__main__":
    unittest.main(verbosity=2)