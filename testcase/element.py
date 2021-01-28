from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement(object):
    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator) #we will wait till the driver will be on the page
        )
        driver.find_element_by_name(self.locator).clear() #we will fimd tjhe object obj and clear it
        driver.find_element_by_name(self.locator).send_keys(value) #and then send the keys value

    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator)
        )
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value") #get the value of the atribute and return that
