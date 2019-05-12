from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time

# todo select you OS (commend device u didn't use)
# Window
browser: WebDriver = webdriver.Chrome("chromedriver.exe")
# Mac OS
# browser: WebDriver = webdriver.Chrome("chromedriver")

# todo write you UserName and Password here don't forget to not let anyone see
user = ""
password = ""

# todo change value at you want
value = 5

browser.get('https://eassess.ku.ac.th/')


def let_pra_mearn(v):
    while True:
        try:
            pra_mern = browser.find_element_by_name("submit")
            pra_mern.send_keys(Keys.RETURN)
            value_select = browser.find_elements_by_xpath("//input[@value='%d']" % v)
            for i in value_select:
                i.click()
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
                print(i)
    let_pra_mearn(value)
    time.sleep(1)

browser.close()
browser.__exit__()
