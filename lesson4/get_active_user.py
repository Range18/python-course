import re


def get_active_user(filename):
    with open(filename, 'r') as file:
        line = file.readline()
        regex = re.compile("^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+")
        d = dict()
        while line != "":
            id = regex.findall(line)[0]
            if id not in d:
                d[id] = 1
            else:
                d[id] += 1
            line = file.readline()
        max_d = 0
        max_id = 0
        for i in d:
            if d[i] > max_d:
                max_id = i
                max_d = d[i]
        return max_id
