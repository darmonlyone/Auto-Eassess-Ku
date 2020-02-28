from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import random
import time

# todo select you OS (commend device u didn't use)
# Window
browser: WebDriver = webdriver.Chrome("chromedriver.exe")
# Mac OS or Other
# browser: WebDriver = webdriver.Chrome("chromedriver")

# todo write you UserName and Password here don't forget to not let anyone see
user = ""
password = ""

# todo change value at you want
# Professor Vote
# 1 Nice
# 2 Any Suggestion
first_value = 1

# todo change value at you want
# Vote yourself and your conductor
# Range 5 good -> 1 Bad
# 0 fro random
final_value = 5

# random rage
randomrange = [4, 5]

browser.get('https://eassess.ku.ac.th/')

def let_pra_mearn(v):
    while True:
        try:
            if v == 0:
                v = random.randrange(randomrange[0], randomrange[1] + 1)
            pra_mern = browser.find_element_by_name("submit")
            pra_mern.send_keys(Keys.RETURN)
            value_select = browser.find_elements_by_xpath("//input[@value='%d']" % v)
            for i in value_select:
                try:
                    i.click()
                except Exception:
                    break
            submit = browser.find_element_by_name("OK")
            submit.send_keys(Keys.RETURN)
        except NoSuchElementException:
            return


account_text = browser.find_element_by_name('account')
password_text = browser.find_element_by_name('password')

account_text.send_keys(user)
password_text.send_keys(password)

submit_but = browser.find_elements_by_class_name("btn")

submit_but[3].send_keys(Keys.RETURN)
but = browser.find_elements_by_class_name("btn")

for i in range(len(but)):
    value = 0
    if i == 0:
        value = first_value
    else:
        value = final_value
    but = browser.find_elements_by_class_name("btn")
    try:
        but[i].click()
    except StaleElementReferenceException:
        try:
            but[i].submit()
        except StaleElementReferenceException:
            try:
                but[i].send_keys(Keys.RETURN)
            except StaleElementReferenceException:
                pass
    let_pra_mearn(value)
    time.sleep(1)

browser.close()
browser.__exit__()
