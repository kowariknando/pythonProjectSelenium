from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains



PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

#driver.get("https://techwithtim.net")
#driver.close() #close the tab
#print(driver.title)

#find elements on a field, enter text and click search (hit enter) clear the element
'''
search = driver.find_element_by_name("s") #we find the search field
#we could clikc in the element with search.click()
search.clear() #we can clear the element before we enter any text
search.send_keys("test") #we type test on thesearch field
#search.send_keys(Keys.RETURN) #we wanna hit enter = RETURN


#print(driver.page_source)

#time.sleep(5) #we make it sleep for 5 secons

driver.quit() #close the entire window

'''


'''
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main")) #we can use By.Name/otherthings
    )
    #here we put what we want to do
    print(main.text)#prints the main text of the web

    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_by_Class_name("entry-summary")
        print(header.text)
except:
    driver.quit()'''


###NAVIGATING On a web: opening, clicking, going back and forward
'''
link = driver. find_element_by_link_text("Python Programming")
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials")) #we can use By.Name/otherthings
    )
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))  # we can use By.Name/otherthings
    )
    element.click()

    driver.back() #we go back on the page
    driver.back()
    driver.back()
    driver.forward() #we can go forward in the page
    

except:
    driver.quit()
'''

#coockie clicker############################

driver.implicitly_wait(5) # we wanna wait 5 sec so the game will be open and load

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1,-1,-1)]

actions = ActionChains(driver)
actions.double_click(cookie) #this will click whereever is the located the mouse () or whereever we specify


#if we dont put actions.perform() the actions wont be executed
for i in range(5000): #we want to perform the actionChangs 5000 times
    actions.perform()
    count = int(cookie_count.text.split(" ")[0]) #we store the amount of cookies that we have
    #print(count)
    for item in items: #miramos el valor de cada upgrade items
        value = int(item.text)
        if value <= count:
            upgrade_action = ActionChains(driver)
            upgrade_action.move_to_element(item) #we move the mouse to the item that we wanna update
            upgrade_action.click() #we click in the item that we wanna upgrade
            upgrade_action.perform()