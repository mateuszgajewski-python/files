lista = []


with open("imionanazwiska.txt","r", encoding = "UTF-8") as file:
    for line in file:        
        lista.append(tuple((line.replace("\n","")).split(" ")))
        

print()

with open("imiona.txt","w", encoding = "UTF-8") as file:
    for krotka in lista:
        file.write(krotka[0] + "\n")

with open("nazwiska.txt","w", encoding = "UTF-8") as file:
    for krotka in lista:
        try:
            file.write(krotka[1] + "\n")
        except:
            file.write("\n")




    


