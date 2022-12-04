# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCotblann():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_cotblann(self):
    self.driver.get("https://www.superprof.fr/")
    self.driver.set_window_size(1280, 680)
    self.driver.find_element(By.CSS_SELECTOR, ".static-content .basic-header-button:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".static-content .basic-header-button:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".focus > input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".focus > input").send_keys("russe.avec.olessia+11@gmail.com")
    self.driver.find_element(By.CSS_SELECTOR, ".focus > input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".focus > input").send_keys("Kiev2022")
    self.driver.find_element(By.CSS_SELECTOR, ".big-button > .text:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".static-content .icon-menu").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".static-content > .header-buttons span:nth-child(2)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.LINK_TEXT, "Tableau de bord").click()
    self.driver.find_element(By.LINK_TEXT, "Mes annonces").click()
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, ".button > span").click()
    self.vars["win6186"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win6186"])
  