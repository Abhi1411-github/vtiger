from selenium.common import NoSuchElementException
from selenium.webdriver.support.select import Select
from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, alert_is_present
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert


def _wait(func):                                           # function decorator
    def wrapper(*args,**kwargs):
        instance = args[0]
        locator = args[1]
        w = WebDriverWait(instance.driver,10)
        v = visibility_of_element_located(locator)
        w.until(v)
        return func(*args,**kwargs)
    return wrapper



class Demo:

    def __init__(self,driver):
        self.driver = driver

    @_wait
    def click_button(self,locator):
        self.driver.find_element(*locator).click()             # locator_name,locator_value = locator

    @_wait
    def text_fill(self,locator,value):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    def change_window(self,index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    def search_enter(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.ENTER).perform()

    def alert_accept(self):
        self.driver.switch_to.alert.accept()

    def alert_dismiss(self):
        self.driver.switch_to.alert.dismiss()

    def cursor_move(self,locator):
        action = ActionChains(self.driver)
        profile = self.driver.find_element(*locator)
        action.move_to_element(profile).perform()

    @_wait
    def select_dropdown(self,locator,index):
        dropdown = self.driver.find_element(*locator)
        sel = Select(dropdown)
        sel.select_by_index(index)

    def drag_drop(self,source_element,target_element):
        locator_1 = self.driver.find_element(*source_element)
        locator_2 = self.driver.find_element(*target_element)
        action = ActionChains(self.driver)
        action.drag_and_drop(locator_1,locator_2).perform()

    def right_click(self,locator):
        action = ActionChains(self.driver)
        action.context_click(*locator).perform()

    def double_click(self,locator):
        action = ActionChains(self.driver)
        action.double_click(*locator).perform()




