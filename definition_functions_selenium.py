import linkfinder.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class Link_finder(webdriver.Chrome):
    def __init__(self, driver_path=r"C:/SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Link_finder,self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()
        

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
    
    def land_first_page(self):
        self.get(const.BASE_URL)
    
    def connexion(self, username, password="Kiev2022"):
        self.driver.find_element(By.CSS_SELECTOR, ".static-content .basic-header-button:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".focus > input").click()
        self.driver.find_element(By.CSS_SELECTOR, ".focus > input").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, ".focus > input").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, ".signin .buttons-container > .big-button").click()
        
    def go_tableaudebord(self):
        element = self.driver.find_element(By.CSS_SELECTOR, ".static-content > .header-buttons span:nth-child(2)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.LINK_TEXT, "Tableau de bord").click()

    def go_annonce(self):
        self.driver.find_element(By.CSS_SELECTOR, ".static-content .avatar-wrapper").click()
        self.driver.find_element(By.LINK_TEXT, "Annonces").click()

    def go_annonce_eleve(self):
        self.driver.find_element(By.CSS_SELECTOR, ".static-content .avatar-wrapper").click()
        self.driver.find_element(By.LINK_TEXT, "Annonces").click()
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.LINK_TEXT, "Voir en tant qu\'élève").click()
        self.vars["win2548"] = self.wait_for_window(2000)
        self.vars["root"] = self.driver.current_window_handle
        self.driver.switch_to.window(self.vars["win2548"])
    
    def tbl_retrieveadress(self):
        adresse = self.driver.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div/div[1]/div[1]/div[3]").text
        return(adresse)
    
    def tbl_retrieveprice(self):
        price = self.driver.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div/div[2]/div[4]/ul/div/li/div[2]/div/span[2]/span[1]").text
        return(price)

    def ann_retrieverecolink(self):
        self.driver.find_element(By.CSS_SELECTOR, ".copy > .chip").click()
        #self.driver.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div/div/main/div/div[1]/div[7]/div[2]/div/input").click()
        lien_reco = pyperclip.paste()
        return(lien_reco)
        