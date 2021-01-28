import unittest
from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):

    def setUp(self): ##this will be the first method to be run
        #setup will be run for each test_
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("https://www.python.org/")

    def test_title(self):
        mainPage = page.MainPage()
        assert mainPage.is_tittle_matches()

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_tittle_matches() #if its true it continues
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found() #if we find any result by searching for the value pycon


    def tearDown(self): #this will run at the end
        self.driver.close() #will close the tab
'''
    def test_example(self): #as we inheritate from unittest TestCase the methods called test_something will be running as tests
        print("testiiiing")
        assert False
''' #test example this should go between setUp and tearDown

if __name__ == "__main__": #if we run this module, that has not being imported
    unittest.main() #this tell us to run all the unit tests that we have defined