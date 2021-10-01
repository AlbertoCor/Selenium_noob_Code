import unittest
from selenium import webdriver

class Typos(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r"C:\Users\Alberto\OneDrive\Platzi\Data_courses\Selenium_wt_python\bin\chromedriver.exe")
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        driver.find_element_by_link_text('Sortable Data Tables').click()


    def test_sort_table(self):
        driver = self.driver

        table_data = [[] for i in range(5)]
        # print(table_data)

        for i in range(5):
            header = driver.find_element_by_xpath(f'//*[@id="table1"]/thead/tr/th[{i + 1}]/span')
            table_data[i].append(header.text)
            for j in range (5):
                row_table = driver.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[1]/td[{j +1}]')
                table_data[i].append(row_table.text)
        
        print(table_data)

if __name__ == "__main__":
    unittest.main(verbosity=2)