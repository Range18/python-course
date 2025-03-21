#!/usr/bin/env python3
import re
from enum import Enum


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'
    Unknown = 'Unknown'


male_names = {
    "Дмитрий", "Александр", "Сергей", "Михаил", "Андрей", "Иван", "Антон",
    "Роман", "Евгений", "Павел", "Владислав", "Василий", "Олег", "Максим",
    "Виктор", "Богдан", "Степан", "Игорь", "Артём", "Алексей", "Юрий", "Глеб",
    "Денис", "Николай", "Всеволод", "Генрик", "Марк", "Виталий", "Арсений",
    "Вадим", "Алехандро", "Борис", "Кирилл"
}

female_names = {
    "Анна", "Мария", "Ольга", "Елена", "Татьяна", "Алиса", "Полина", "София",
    "Кристина", "Лилия", "Юлия", "Надежда", "Екатерина", "Анастасия", "Тамара",
    "Евгения", "Светлана", "Наталья"
}

female_suffixes = ["ова", "ева", "ина", "ая", "ская", "цкая", "их", "ых"]
male_suffixes = ["ов", "ев", "ин", "ский", "цкий", "ун", "дян", "ян"]


def determine_gender_by_name_and_surname(name, surname):
    name = name.capitalize()
    surname = surname.lower()

    if name in male_names:
        return Gender.Male
    elif name in female_names:
        return Gender.Female

    if any(surname.endswith(suffix) for suffix in female_suffixes):
        return Gender.Female
    elif any(surname.endswith(suffix) for suffix in male_suffixes):
        return Gender.Male

    return Gender.Unknown


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


def create_persons(content):
    years_and_names = []
    current_year = 0
    year_regex = re.compile(r"<h3>(\d{4})</h3>")
    name_surname_regex = re.compile(r"<a href=[\s\S]*?/>([\s\S]*?)</a>")

    for line in content:
        year_match = year_regex.search(line)
        if year_match:
            current_year = year_match.group(1)
        surname_name = name_surname_regex.findall(line)
        if surname_name:
            years_and_names.append(Person(surname_name[0], current_year))
    return years_and_names


def make_stat(filename):
    """
    Функция вычисляет статистику по именам за каждый год с учётом пола.
    """
    with open(filename, encoding="cp1251") as file:
        content = file.readlines()
        return create_persons(content)


def extract_years(stat):
    """
    Функция принимает на вход вычисленную статистику и выдаёт список годов,
    упорядоченный по возрастанию.
    """
    years = []
    for person in stat:
        if person.year not in years:
            years.append(person.year)
    return sorted(years)


def extract_general(stat, gender=None):
    """
    Функция принимает на вход вычисленную статистику и выдаёт список tuple'ов
    (имя, количество) общей статистики для всех имён.
    Список должен быть отсортирован по убыванию количества.
    """
    stat_by_names = dict()
    for person in stat:
        if gender == person.gender if gender else True:
            if person.name not in stat_by_names:
                stat_by_names.setdefault(person.name, 0)
            stat_by_names[person.name] += 1
    return sorted(stat_by_names.items(), key=lambda x: x[1], reverse=True)


def extract_general_male(stat):
    """
    Функция принимает на вход вычисленную статистику и выдаёт список tuple'ов
    (имя, количество) общей статистики для имён мальчиков.
    Список должен быть отсортирован по убыванию количества.
    """
    return extract_general(stat, Gender.Male)


def extract_general_female(stat):
    """
    Функция принимает на вход вычисленную статистику и выдаёт список tuple'ов
    (имя, количество) общей статистики для имён девочек.
    Список должен быть отсортирован по убыванию количества.
    """
    return extract_general(stat, Gender.Female)


def extract_year(stat, year, gender=None):
    """
    Функция принимает на вход вычисленную статистику и год.
    Результат — список tuple'ов (имя, количество) общей статистики для всех
    имён в указанном году.
    Список должен быть отсортирован по убыванию количества.
    """
    stat_by_year = dict()
    for person in stat:
        if person.year == year and (
                gender == person.gender if gender else True):
            if person.name not in stat_by_year:
                stat_by_year.setdefault(person.name, 0)
            stat_by_year[person.name] += 1
    return sorted(stat_by_year.items(), key=lambda x: x[1], reverse=True)


def extract_year_male(stat, year):
    """
    Функция принимает на вход вычисленную статистику и год.
    Результат — список tuple'ов (имя, количество) общей статистики для всех
    имён мальчиков в указанном году.
    Список должен быть отсортирован по убыванию количества.
    """
    return extract_year(stat, year, Gender.Male)


def extract_year_female(stat, year):
    """
    Функция принимает на вход вычисленную статистику и год.
    Результат — список tuple'ов (имя, количество) общей статистики для всех
    имён девочек в указанном году.
    Список должен быть отсортирован по убыванию количества.
    """
    return extract_year(stat, year, Gender.Female)


if __name__ == '__main__':
    pass
