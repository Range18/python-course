import requests
import re


def count_names(names_arr):
    names_dict = dict()
    for el in names_arr:
        surname, name = el.split(' ')
        if name in names_dict:
            names_dict[name] += 1
        names_dict.setdefault(name, 1)
    return names_dict


def main():
    html = requests.get(
        'https://raw.githubusercontent.com/python-fiit/public-materials/refs/heads/master/02-basictypes/hw/hw2/home.html')
    names_arr = []
    for line in html.text.split('\n'):
        name_surname = re.findall(r"<a href=[\s\S]*?/>([\s\S]*?)</a>", line)
        if name_surname:
            names_arr.append(name_surname[0])
    print(count_names(names_arr))


if __name__ == '__main__':
    main()
