a = 5


with open("test2", "w") as file:
    file.write("sample")
    print(0/0)
    a = 5
    file.write("sample2")
