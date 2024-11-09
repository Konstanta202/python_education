class Person:
   def __init__(self, age):
       self.age_ = age

   @property
   def age(self):
       return self.age_

   @age.setter
   def age(self, value):
       if value < 0:
           self.age_ = 0
       else:
           self.age_ = value


code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)

if __name__ == '__main__':
    person = Person(18)
    person.age = -19
    print(person.age)