import csv, unittest
from ddt import ddt, data, unpack
from selenium import webdriver

# function to read files csv data 
def get_data(file_name):
    rows = []
    data_file = open(file_name, "r")
    reader = csv.reader(data_file)
    next(reader, None) # make exception to use 1st line of excel

    for row in reader:
        rows.append(row)
    return rows

@ddt
class SearchCsvDDT(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r"C:\Users\Alberto\OneDrive\Platzi\Data_courses\Selenium_wt_python\bin\chromedriver.exe")
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")

    @data(*get_data('./scripts/data/testdata.csv'))
    @unpack

    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        # locate html location of products showed (use class location tree holder elements by h2)
        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')
        
        # convert any data from csv to integer type
        expected_count = int(expected_count)

        # we code an option if search not reurn values (optional, already webage return a 
        # message if dont found anything by search textbox)
        if expected_count > 0:
            self.assertEqual(expected_count, len(products))
        else:
            message = driver.find_element_by_class_name('note-msg')
            self.assertEqual("Your search returns no results.", message)

        print(f'found {len(products)} products.')

    def tearDown(self):
        self.driver.close()
        

if __name__ == "__main__":
    # we could type verbosity to get more information
    unittest.main()