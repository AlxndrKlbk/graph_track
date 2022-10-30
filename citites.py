import json
from copy import deepcopy


def processing():
    def next_word(j, letter):
        nonlocal operative_cities, total_len
        global result

        while True:
            j += 1

            if j < total_len:
                next_city = operative_cities[j]
                if next_city[-1] == letter:
                    result.append(next_city)
            else:
                break

    def get_current_word():
        nonlocal operative_cities, total_len
        global result
        j = 0
        while True:
            pass

    global cities

    operative_cities = deepcopy(cities)
    total_len = operative_cities.len()

    for i, city in enumerate(operative_cities):
        result_sequence = list()

        result_sequence.append(city)
        next_word(i + 1, city[-1])


with open('input.json', 'r', encoding='utf-8') as jdata:
    cities = json.load(jdata)

result = list()
processing()
