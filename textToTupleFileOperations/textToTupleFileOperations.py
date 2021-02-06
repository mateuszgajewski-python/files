
data = []

with open("lista.txt", "r", encoding = "UTF-8") as file:
    for line in file:
        x = tuple(line.split())
        data.append(x)      

with open("imiona.txt", "w", encoding = "UTF-8") as file:
    for item in data:
        file.write(item[0] + "\n")

with open("nazwiska.txt", "w", encoding = "UTF-8") as file:
    for item in data:
        try:
            file.write(item[1] + "\n")
        except IndexError:
            file.write("\n")

    
