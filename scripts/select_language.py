import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select # tool for selecting dropdown

class LanguageOptions(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r"C:\Users\Alberto\OneDrive\Platzi\Data_courses\Selenium_wt_python\bin\chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")

    def test_select_language(self):
        exp_option = ['English', 'French', 'German']
        act_option =  []

        select_language = Select(self.driver.find_element_by_id('select-language'))

        # verify #total elements in dropdown
        self.assertEqual(3, len(select_language.options))

        # add to empty array the data of dropdown
        for option in select_language.options: # .options method enter to the dropdown elements
            act_option.append(option.text)

        # verify list expose and active are identic
        self.assertListEqual(exp_option, act_option)

        # default idiom english verify
        self.assertEqual('English', select_language.first_selected_option.text)

        select_language.select_by_visible_text('German')

        # from some text found then select german take text ans use it to verify selected idiom
        self.assertTrue('store=german' in self.driver.current_url)

        # select idiom by its index number to return english idiom
        select_language = Select(self.driver.find_element_by_id('select-language'))
        select_language.select_by_index(0)

    def tearDown(self):
        self.driver.implicitly_wait(30)
        self.driver.close()
        

if __name__ == "__main__":
    unittest.main(verbosity=2)