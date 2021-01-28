from locator import *
from element import BasePageElement


#lets say there is an element on the page we wanna access:
class SearchTextElement(BasePageElement):
    locator = "q" #the ID name of Python website of the serach field is q
''' 
class GoButtonElement(BasePageElement):
    locator = "go" #the element that we wanna find has locator "go" and as the class is inheritante from BasePageElement this would be enought to find the element
''' #imagine that we wanna find the element go button we would do:

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage): #it will take the init from BasePage

    search_text_element = SearchTextElement()

    def is_tittle_matches(self): #check if the title matches the title that we want
        return "Python" in self.driver.title #check  if the Python string is on the title of driver

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON) # the * before the tuple split the elements of the tuple
        element.click()

class SearchResultPage(BasePage):
    def is_results_found(self):
        return "No results found." not in self.driver.page_source