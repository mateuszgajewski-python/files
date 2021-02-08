plik="zadanie.txt"



def otwieraniePliku(nazwa):
    try:
        with open(nazwa, "r", encoding = "UTF-8") as file:
            zawartoscPliku = file.read()
            return zawartoscPliku
    except FileNotFoundError:
        return ("plik nie istnieje")


print(otwieraniePliku(plik))
        
