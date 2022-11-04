import json
from pprint import pprint

def check_adjancency(word: str, sub_word: str) -> int:
    last_letter = word[-1] if word[-1] not in ('ь', 'ъ') else word[-2]

    if last_letter == sub_word[0]:
        return 1
    else:
        return 0


def pathfinder(current_top: int):
    global adjacency_matrix, size, visited_tops

    for j, new_top in enumerate(adjacency_matrix[current_top]):
        if new_top == 0:
            continue
        else:
            if j in visited_tops:
                continue
            else:
                visited_tops.append(j)
                if len(visited_tops) == size:
                    return True

                ended = pathfinder(j)
                
                if ended:
                    return True
                visited_tops = visited_tops[0:visited_tops.index(j)]

    if len(visited_tops) < size:
        return False
    return True
            

def start_pathfinding():
    global visited_tops
    for i in range(size):
        visited_tops = [i]
        ended = pathfinder(i)
        
        if ended:
            break
        else:
            continue

    print(','.join([init_cities[i] for i in visited_tops]))


if __name__ == '__main__':
    with open('input.json', 'r', encoding='utf-8') as jdata:
        init_cities = json.load(jdata)

    size = len(init_cities)
    cities = [init_cities[i].lower() for i in range(size)]
    adjacency_matrix = [[0 if i == j else check_adjancency(word, sub_word) for j, sub_word in enumerate(cities)]
                        for i, word in enumerate(cities)]
    pprint(adjacency_matrix) 
    visited_tops = list()
    start_pathfinding()

