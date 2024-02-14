import csv


def hash_creator(arr):
    '''
    hash_creator создаёт hash для переданного словаря

    aplhabet  - алфавит со всеми возможными символами, который могут встретится в названиях и именах персонажей
    p - значение p
    m - значение м
    game - название игры без пробелов
    character - имя персонажа без пробелов
    hash - хэш

    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet += '1234567890'
    alphabet += ":-'.,"
    apl_dict = {alphabet[i]: i + 1 for i in range(len(alphabet))}
    p, m = 68, 10**9 + 9
    game = arr['GameName'].replace(' ', '')
    character = arr['characters'].replace(' ', '')
    line = game + character
    hash = 0
    for i in range(len(line)):
        hash += apl_dict[line[i]] * p**i 
    return hash % m


with open('game.txt', 'r', encoding='UTF-8') as file:
    characters_list = list(csv.DictReader(file, delimiter='$'))
    for s in characters_list:
        s['id'] = hash_creator(s)

with open('game_with_hash.csv', 'w', encoding='UTF-8') as file:
    writer = csv.DictWriter(f=file, fieldnames=['id', 'GameName', 'characters', 'nameError', 'date'], delimiter='$')
    writer.writerow({'id': 'id', 'GameName': 'GameName', 'characters': 'characters', 'nameError': 'nameError', 'date': 'date'})
    writer.writerows(characters_list)
    
    
