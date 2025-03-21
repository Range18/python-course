from hw_2.determine_gender_by_surname import \
    determine_gender_by_name_and_surname
from hw_2.genders_enum import Gender


class Person:
    def __init__(self, surname_name, year):
        surname, name = surname_name.split(' ')
        self._name = name
        self._surname = surname
        self._year = year
        self._gender = determine_gender_by_name_and_surname(name, surname)

    def __str__(self):
        return f"{self.surname} {self.name} {self.year} {self.gender}"

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def year(self):
        return self._year

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    @year.setter
    def year(self, value):
        self._year = value

    @surname.setter
    def surname(self, value):
        self._surname = value

    @name.setter
    def name(self, value):
        self._name = value
