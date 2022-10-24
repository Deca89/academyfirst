class Person:

    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age
    
    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age
    
    @name.setter
    def name(self, rename):
        self.__name = rename
    
    @age.setter
    def name(self, renage: int):
        self.__age = renage

    def __gt__(self, another_person):
        return self.age > another_person.age