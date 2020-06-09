class Friend:
    def __init__(self, name="Goda", age="15", gender="f"):
        self.name = name
        self.age = age
        self.gender = gender

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    def to_string(self):
        print("My name is %s" % (self.__name))

    def formatted_to_string(self):
        return "My name is {} and I am {} years old".format(self.__name, self.__age)

    # this is actually the toString of python
    def __str__(self):
        return "My name is {} and I am {} years old".format(self.__name, self.__age)

    def __gt__(self, friend2):
        if self.__age > friend2.age:
            return True
        else:
            return False


goda = Friend("Goda", 15, "f")
tanu = Friend("Tanu", 14, "f")
goda.to_string()
tanu.to_string()

print(tanu.formatted_to_string())

print(str(goda))

print(goda > tanu)


class Girl(Friend):
    def __init__(self, name, age, gender, valid):
        Friend.__init__(self, name, age, gender)
        self.__valid = valid

    @property
    def valid(self):
        return self.__valid

    @valid.setter
    def valid(self, valid):
        self.__valid = valid

    def __str__(self):
        return super().__str__() + " and am I a girl? " + str(self.__valid)


tanu2 = Girl("Tanu", 15, "f", True)
print(tanu2.__str__())
