from easygui import *
import sys
import csv

#create database, however overwrites it every time
#with open("C://db.csv", 'w+', newline=''):
#    print("succesfully created db")

#landing scherm
title1 = "Welkom"
msg = "Welkom in bij kamer reserveringstool"
button = ["OK", "Annuleer"]
output = ccbox(msg, title1, button)


if output == True:

#code voor datum keuze
        title2 = "Datum keuzemenu"
        choices = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag"]
        msg = "Kies een dag"
        reply = choicebox(msg, title2, choices = choices)
        button = ["OK", "Annuleer"]

        print("You selected:", end = "")
        print(reply)
        
        if reply:

#code voor ruimte keuze
            options = ["Kamer 1", "Kamer 2", "Kamer 3", "Cancel"]
            button = buttonbox("Kies een kamer", title = "kamers", choices = options)
            if button == options[3]:
                sys.exit()
                
         
#tijdslot kiezen         
            message = "Selecteer de gewenste periode:"
            title = "Tijdsslot selecteren"
            Tijd = ["Ochtend", "Middag", "Avond","Annuleer"]
            output = buttonbox(message, title, Tijd)
            print(output)
            if output == Tijd[3]:
                sys.exit()
            print(output)
            total = [reply,button,output]
            with open("C://db.csv", 'r+', newline='') as db:
                    reader = csv.reader(db, delimiter=',')
                    if total not in reader:
                            writer = csv.writer(db)
                            writer.writerow(total)
                    else:
                        error = "geselecteerde datum en tijdslot al in gebruik"
                        msgbox(error)
                        sys.exit()
            
# opslaan success
                    success = "Resevering succesvol opgeslagen"
                    final = msgbox (success, title = "Succesvol opgeslagen")

                    print(final, end = "")
                    print(reply)






