class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        # self.set_age(age)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Invalid age")
        self._age = age

    '''
    def get_age(self):
        return self._age

    def set_age(self, age):
        if age < 0 :
            raise ValueError("invalid age")
        self._age = age
    age = property(get_age, set_age)
    # 이렇게 하면 왼쪽이 getter 오른쪽 setter로 설정해서 밖에서 age. 로 get도 되고 set도 자동으로 됨
    '''


if __name__ == '__main__':
    person = Person("seyeon", "park", 20)
    # print(person.get_age())
    print(person.age)
    try:
        # person.set_age(-1)
        person.age = -1
    except:
        print('error')

    # person.set_age(person.get_age() + 1)
    person.age = person.age + 1
    print(person.age)


# https://www.daleseo.com/python-property/