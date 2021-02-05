uczniowie = [
                ("Jan Kowalski"),
                ("Adam"),
                ("Kamil Stoch"),
                ("Jakub Janda"),
                ("Michal Wisniewski")
            ]



def dzielenieWyrazow(lista):
    
    listka = []
    
    for x in lista:
        
        x1 = x.split()
        if (len(x1)==1):
            x1.append("")
            
        listka.append(x1)
        
        
    return listka






arg = dzielenieWyrazow(uczniowie)


imiona = [x for x,y in arg]

nazwiska = [y for x,y in arg if y!=""]


for x in uczniowie:
    print(x)
print("\n")
for x in imiona:
    print(x)
print("\n")
for x in nazwiska:
    print(x)




        


