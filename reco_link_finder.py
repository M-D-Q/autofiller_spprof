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

## get la liste des identifiants


i=0

#liste_email = get_stuff_from_csv('id.csv')
liste_email = ['russe.avec.olessia+un@gmail.com', 'russe.avec.olessia+2@gmail.com', 'russe.avec.olessia+3@gmail.com', 'russe.avec.olessia+4@gmail.com', 'russe.avec.olessia+5@gmail.com', 'russe.avec.olessia+6@gmail.com', 'russe.avec.olessia+7@gmail.com', 'russe.avec.olessia+8@gmail.com', 'russe.avec.olessia+9@gmail.com', 'russe.avec.olessia+10@gmail.com', 'russe.avec.olessia+11@gmail.com', 'russe.avec.olessia+12@gmail.com', 'russe.avec.olessia+13@gmail.com', 'russe.avec.olessia+14@gmail.com', 'russe.avec.olessia+15@gmail.com', 'russe.avec.olessia+16@gmail.com', 'russe.avec.olessia+17@gmail.com', 'russe.avec.olessia+51@gmail.com', 'russe.avec.olessia+52@gmail.com', 'russe.avec.olessia+53@gmail.com', 'russe.avec.olessia+57@gmail.com', 'russe.avec.olessia+58@gmail.com', 'russe.avec.olessia+59@gmail.com', 'russe.avec.olessia+60@gmail.com', 'russe.avec.olessia+61@gmail.com', 'russe.avec.olessia+74@gmail.com', 'russe.avec.olessia+75@gmail.com', 'russe.avec.olessia+76@gmail.com', 'russe.avec.olessia+77@gmail.com', 'russe.avec.olessia+78@gmail.com', 'russe.avec.olessia+79@gmail.com', 'russe.avec.olessia+81@gmail.com', 'russe.avec.olessia+87@gmail.com', 'russe.avec.olessia+89@gmail.com', 'russe.avec.olessia+90@gmail.com', 'russe.avec.olessia+91@gmail.com', 'russe.avec.olessia+92@gmail.com', 'russe.avec.olessia+93@gmail.com', 'russe.avec.olessia+94@gmail.com', 'russe.avec.olessia+95@gmail.com', 'russe.avec.olessia+96@gmail.com', 'russe.avec.olessia+97@gmail.com', 'russe.avec.olessia+98@gmail.com', 'russe.avec.olessia+99@gmail.com', 'russe.avec.olessia+100@gmail.com']
print (liste_email)
for chocolat in liste_email :

    ##### infos Login
    email = liste_email[i]
    password = "Kiev2022"
    id_compte = email_split(email)


    #lancement du browser et get superprof.fr
    #url = str(input("URL ?"))
    url = "https://www.superprof.fr/"
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(url)
    browser.maximize_window()

    

    #click sur le bouton "connexion"
    browser.find_element(By.XPATH, value="/html/body/div[2]/div[1]/header/div[1]/div[3]/button").click()

    #renseigner adresse email et mdp
    time.sleep(3)
    browser.find_element(By.XPATH, value="/html/body/div[2]/div[5]/div/div/div[2]/div/div[4]/div[1]/div/form/div[1]/input").send_keys(str(email))
    #WebDriverWait(browser, 5).until(EC.element_to_be_clickable(By.XPATH, value="/html/body/div[2]/div[5]/div/div/div[2]/div/div[4]/div[1]/div/form/div[1]/input")).send_keys(str(email))
    browser.find_element(By.XPATH, value="/html/body/div[2]/div[5]/div/div/div[2]/div/div[4]/div[1]/div/form/div[2]/input").send_keys(str(password))
    browser.find_element(By.XPATH, value="/html/body/div[2]/div[5]/div/div/div[2]/div/div[4]/div[2]/div[1]/div[2]").click()
    # Connexion Reussie

    ##### go tableau de bord
    #browser.find_element(By.XPATH, value="/html/body/div[2]/div[1]/header/div[1]/div[3]/button/div/div[1]").click()
    time.sleep(1)
    #browser.find_element(By.XPATH, value="/html/body/div[2]/div[1]/header/div[3]/div[1]/ul/li[1]").click()
    #browser.find_element(By.CSS_SELECTOR, ".static-content .avatar-wrapper").click()
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".static-content .avatar-wrapper"))).click()
    browser.find_element(By.LINK_TEXT, "Tableau de bord").click()

    #browser.get("https://www.superprof.fr/tableau-de-bord.html")
    time.sleep(3)
    ## get adresse
    adresse = browser.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div/div[1]/div[1]/div[3]").text
    print(adresse)
    ##get price
    price = browser.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div/div[2]/div[4]/ul/div/li/div[2]/div/span[2]/span[1]").text
    print(price)

    #Link pour annonces
    #browser.get("https://www.superprof.fr/tableau-de-bord.html/annonces/liste/")
    browser.find_element(By.CSS_SELECTOR, ".static-content .icon-menu").click()
    browser.find_element(By.LINK_TEXT, "Annonces").click()

    #choper le lien de reco
    browser.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div/div/main/div/div[1]/div[7]/div[2]/div/input").click()
    lien_reco = pyperclip.paste()
    print(lien_reco)
    time.sleep(1)
    #voir en tant qu'eleve et prendre le nombre d'avis
    #browser.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div/div/main/div/div[2]/div[2]/div[2]/a").click()
    #browser.find_element(By.LINK_TEXT, "Voir en tant qu\'élève").click()
    try :
 
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Voir en tant qu\'élève"))).click()
        nb_reco = browser.find_element(By.XPATH, value="/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div[4]/div[1]/div[2]/span[2]").text
        print(nb_reco)
    except Exception as e: 
        print(e)
        nb_reco = 0
    


    browser.quit()

    #get la date d'aujourd'hui
    today = str(date.today())

        # python object to be appended
    y = {"id": id_compte,
        "email": email,
        "mdp": password,
        "ville": adresse,
        "reco_link":lien_reco,
        "reco_count":nb_reco,
        "price":price,
        "date_modif":today
        }

    write_json(y,'accounts.json')
    i+=1
    print("""c'etait la procédure numero : """ + str(i))

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
