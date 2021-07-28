class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        # self.age = age
        self.set_age(age)

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age < 0 :
            raise ValueError("invalid age")
        self._age = age



if __name__ == '__main__':
    person = Person("seyeon", "park", 20)
    print(person.get_age())

    try:
        person.set_age(-1)
    except:
        print('error')

    person.set_age(person.get_age() + 1)
    print(person.get_age())


#https://www.daleseo.com/python-property/