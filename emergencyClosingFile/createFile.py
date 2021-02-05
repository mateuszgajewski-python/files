a = 5


try:
    file = open("test", "w")
    file.write("sample")

    print(0/0)

    file.write("sample1")

finally:        
    file.close()
