with open("oceany.txt", "r", encoding = "UTF-8") as file1:    
    
    oceany = file1.read()
    

    print(oceany)

  
with open("oceany2.txt", "r", encoding = "UTF-8") as file2:    
    
    

    oceanyWliscie = file2.read().splitlines()
    print(oceanyWliscie)

 
with open("oceany3.txt", "r", encoding = "UTF-8") as file3:    

    print("\n")
    ocean1 = file3.readline()

    print(ocean1)
    
    ocean2 = file3.readline()

    print(ocean2)

    ocean3 = file3.readline()

    print(ocean3)
    
    ocean4 = file3.readline()

    print(ocean4)

    ocean5 = file3.readline()

    print(ocean5)
    


    

with open("oceany4.txt", "r", encoding = "UTF-8") as file4:

    oceany2 = file4.readlines()

    print(oceany2)

    
print()

with open("oceany5.txt", "r", encoding = "UTF-8") as file5:
    for line in file5:
        print(line)

    
    
    

