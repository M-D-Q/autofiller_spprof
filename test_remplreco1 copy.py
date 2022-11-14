from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import time
from datetime import date
from selenium.webdriver.chrome.options import Options
import json
from definition_fonctions import *
import pyperclip

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

url = "https://www.superprof.fr/"
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get(url)
browser.maximize_window()

browser.get("https://www.superprof.fr/ir/20254091-94c20e")
browser.set_window_size(1550, 830)
browser.find_element(By.ID, "why_him").click()
browser.find_element(By.ID, "why_him").send_keys("Olessia est une super prof, très méthodique et axée résultat, tout en étant fun et décontractée!")
browser.find_element(By.NAME, "submit").click()
time.sleep(2)
browser.find_element(By.CSS_SELECTOR, ".signup .buttons-container > .big-button").click()
#bouton email
browser.find_element(By.CSS_SELECTOR, "div.popin-content:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)").click()
#browser.find_element(By.CSS_SELECTOR, ".focus > input").click()

#prenom
browser.find_element(By.CSS_SELECTOR, ".names-wrapper > div:nth-child(1) > input:nth-child(2)").send_keys("Jean")
#nom
browser.find_element(By.CSS_SELECTOR, ".names-wrapper > div:nth-child(2) > input:nth-child(2)").send_keys("Dehuys")

browser.find_element(By.NAME, "email").send_keys("jean.dehuys78@gmail.com")
browser.find_element(By.NAME, "password").send_keys("Ravlyk2022")
#reclick inscription email
browser.find_element(By.CSS_SELECTOR, "div.popin-content:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)").click()
#browser.find_element(By.CSS_SELECTOR, ".signup .buttons-container > .big-button").click()
#browser.find_element(By.CSS_SELECTOR, ".pg-global-content").click()
time.sleep(5)

