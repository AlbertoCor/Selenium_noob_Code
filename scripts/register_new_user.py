import unittest
from selenium import webdriver

# Main object class to register new user
class RegisterNewUser(unittest.TestCase):
    
    # here define extension for driver (path, settings of objective and web to automate)
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Alberto\OneDrive\Platzi\Data_courses\Selenium_wt_python\bin\chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")

    # sequence for automate, locating html components and verify (assert) elements to be automated, at least send data.
    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_link_text('Log In').click()
        
        create_account_button = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

        self.assertEqual('Create New Customer Account', driver.title)
        
        first_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email_adress = driver.find_element_by_id('email_address')
        news_letter_subscription = driver.find_element_by_id('is_subscribed')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button')

        # ensure text box are enabled
        self.assertTrue(first_name.is_enabled()
        and middle_name.is_enabled()
        and last_name.is_enabled()
        and email_adress.is_enabled()
        and news_letter_subscription.is_enabled()
        and password.is_enabled()
        and confirm_password.is_enabled()
        and submit_button.is_enabled()
        )

        # send data to text box
        first_name.send_keys('test')
        # driver.implicitly_wait(1)
        middle_name.send_keys('test')
        # driver.implicitly_wait(1)
        last_name.send_keys('test')
        # driver.implicitly_wait(1)
        email_adress.send_keys('test@testing.com')
        # driver.implicitly_wait(1)
        password.send_keys('test')
        # driver.implicitly_wait(1)
        confirm_password.send_keys('test')
        # driver.implicitly_wait(2000)
        submit_button.click()
        # driver.implicitly_wait(2000)

    def tearDown(self):
        self.driver.implicitly_wait(15)
        self.driver.close()
        

if __name__ == "__main__":
    unittest.main(verbosity=2)