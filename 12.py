def определение_старшего_возраста(возраст1, возраст2):
    if возраст1 > возраст2:
        return возраст1
    else:
        return возраст2

возраст_Егора = 25
возраст_Киры = 30
возраст_Вани = 20

старший_возраст = определение_старшего_возраста(возраст_Егора, возраст_Киры)
print("Самый старший возраст:", старший_возраст)

старший_возраст = определение_старшего_возраста(возраст_Егора, возраст_Вани)
print("средний возраст:", старший_возраст)