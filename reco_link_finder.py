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
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#lancement du browser et get superprof.fr
#url = str(input("URL ?"))
url = "https://www.superprof.fr/"
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get(url)
browser.maximize_window()

#####Login
username = "XXX"
password = "XXX"

#click sur le bouton "connexion"
browser.find_element(By.XPATH, value="/html/body/div[2]/div[1]/header/div[1]/div[3]/button").click()

#renseigner adresse email et mdp
browser.find_element(By.XPATH, value="/html/body/div[2]/div[5]/div/div/div[2]/div/div[4]/div[1]/div/form/div[1]/input").send_keys(str(username))
browser.find_element(By.XPATH, value="/html/body/div[2]/div[5]/div/div/div[2]/div/div[4]/div[1]/div[2]/form/div[2]/input").send_keys(str(password))
browser.find_element(By.XPATH, value="/html/body/div[2]/div[5]/div/div/div[2]/div/div[4]/div[2]/div[1]/div[2]").click()
# Connexion Reussie

##### go tableau de bord
browser.get("https://www.superprof.fr/tableau-de-bord.html")

browser.quit()




#Link pour annonces
#https://www.superprof.fr/tableau-de-bord.html/annonces/liste/

#Xpath du lien recommandation
#/html/body/div[1]/div[2]/div/div/main/div/div[1]/div[7]/div[2]/div/input
# A capturer et rentrer dans le json

#Xpath du bouton "voir en tant qu'eleve"
#/html/body/div[1]/div[2]/div/div/main/div/div[2]/div[2]/div[2]/a

#Xpath du texte 'nombre d'avis'
#/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div[4]/div[1]/div[2]/span[2]
# A capturer et rentrer dans le json

#Xpath du field address 'Nice, France' : /html/body/div[1]/div[2]/div/div[1]/div[1]/div[3]
#trouvable sur le tableau de bord : https://www.superprof.fr/tableau-de-bord.html
