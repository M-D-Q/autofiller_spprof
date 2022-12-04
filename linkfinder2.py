import time
from datetime import date
import json
from definition_fonctions import *
from definition_functions_selenium import *

url = "kek"
i=0

#liste_email = get_stuff_from_csv('id.csv')
liste_email = ['russe.avec.olessia+un@gmail.com', 'russe.avec.olessia+2@gmail.com', 'russe.avec.olessia+3@gmail.com', 'russe.avec.olessia+4@gmail.com', 'russe.avec.olessia+5@gmail.com', 'russe.avec.olessia+6@gmail.com', 'russe.avec.olessia+7@gmail.com', 'russe.avec.olessia+8@gmail.com', 'russe.avec.olessia+9@gmail.com', 'russe.avec.olessia+10@gmail.com', 'russe.avec.olessia+11@gmail.com', 'russe.avec.olessia+12@gmail.com', 'russe.avec.olessia+13@gmail.com', 'russe.avec.olessia+14@gmail.com', 'russe.avec.olessia+15@gmail.com', 'russe.avec.olessia+16@gmail.com', 'russe.avec.olessia+17@gmail.com', 'russe.avec.olessia+51@gmail.com', 'russe.avec.olessia+52@gmail.com', 'russe.avec.olessia+53@gmail.com', 'russe.avec.olessia+57@gmail.com', 'russe.avec.olessia+58@gmail.com', 'russe.avec.olessia+59@gmail.com', 'russe.avec.olessia+60@gmail.com', 'russe.avec.olessia+61@gmail.com', 'russe.avec.olessia+74@gmail.com', 'russe.avec.olessia+75@gmail.com', 'russe.avec.olessia+76@gmail.com', 'russe.avec.olessia+77@gmail.com', 'russe.avec.olessia+78@gmail.com', 'russe.avec.olessia+79@gmail.com', 'russe.avec.olessia+81@gmail.com', 'russe.avec.olessia+87@gmail.com', 'russe.avec.olessia+89@gmail.com', 'russe.avec.olessia+90@gmail.com', 'russe.avec.olessia+91@gmail.com', 'russe.avec.olessia+92@gmail.com', 'russe.avec.olessia+93@gmail.com', 'russe.avec.olessia+94@gmail.com', 'russe.avec.olessia+95@gmail.com', 'russe.avec.olessia+96@gmail.com', 'russe.avec.olessia+97@gmail.com', 'russe.avec.olessia+98@gmail.com', 'russe.avec.olessia+99@gmail.com', 'russe.avec.olessia+100@gmail.com']
print (liste_email)
for chocolat in liste_email :

    with Link_finder() as bot :
        bot.land_first_page(url)
        





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
    osef = input("Press Enter to continue...")