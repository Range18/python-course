import requests


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
    text = html.text
    names_arr = []
    for line in text.split('\n'):
        if '<a href=' in line:
            name_start_ind = line.find('<a href=')
            name_start_ind += line[name_start_ind + 8:].find('/>')
            name = line[name_start_ind + 2:line.find('</a>')]
            names_arr.append(name)
    print(count_names(names_arr))


if __name__ == '__main__':
    main()
