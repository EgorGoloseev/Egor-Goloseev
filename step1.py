class Student:

   def __init__(self, name , age):
       self.name = name
       self.age = age



   def you_self(self):
       print(f'Меня зовут{self.name}, мне {self.age}лет')


s = Student( name= 'Алексей' , age= 25)
s.you_self()