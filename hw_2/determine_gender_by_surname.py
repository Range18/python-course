from hw_2.genders_enum import Gender

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
