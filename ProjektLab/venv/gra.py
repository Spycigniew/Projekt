import random
import time

gra = ["kamien", "papier", "nozyce"]

user = "start"
while user!="koniec":

    user = input("kamien, papier , nozyce     ")
    if user == "koniec":
        print("koniec")
        continue
    if user != "kamien" and user != "nozyce" and user !="papier":
        print("Wpisz papaier,kamien,nozyce ")
        continue
    komputer = random.choice(gra)
    print(komputer)
    if user == komputer:
        print("remis")
    if user == "kamien":
        if komputer =="papier":
            print("przegrana")
        elif komputer =="nozyce":
            print("wygrana")
    if user == "papier":
        if komputer == "nozyce":
            print("przegrana")
        elif komputer == "kamien":
            print("wygrana")

    if user == "nozyce":
        if komputer == "kamien":
            print("przegrana")
        elif komputer == "papier":
            print("wygrana")
