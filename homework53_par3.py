import datetime

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.lat_name = last_name

class Baby(Person):
    def speak(self):
        print('Бла-бла-бла')


class Adult(Person):
    def speak(self):
        print('Привіт мене звати', self.first_name)

class Calendar:
    def book_appointment(self, date):
        print('Бронювання прийому на дату', date)

class OrganizeAdult(Adult, Calendar):
    pass

class OrganizedBaby(Baby, Calendar):
    def book_appointment(self, date):
        print('Зверніть увагу, що ви записуєтесь на прийом')

andres = OrganizeAdult('Андрес', 'Гомес')
boris = OrganizedBaby('Борис', 'Бамблтон')

andres.speak()
boris.speak()
boris.book_appointment(datetime.date(2018, 1, 1))