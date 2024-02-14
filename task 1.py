import csv

with open('game.txt', 'r', encoding='UTF-8') as file:
    characters_list = list(csv.DictReader(file, delimiter='$'))
    for s in characters_list:
        if '55' in s['nameError']:
            print(f'У персонажа {s["characters"]} в игре {s["GameName"]} нашлась ошибка с кодом {s["nameError"]}. Дата фиксации: {s["date"]}')
            s['nameError'] = 'Done'
            s['date'] = '0000-00-00'

with open('game_new.csv', 'w', encoding='UTF-8') as file:
    writer = csv.DictWriter(f=file, fieldnames=['GameName', 'characters', 'nameError', 'date'], delimiter='$')
    writer.writerow({'GameName': 'GameName', 'characters': 'characters', 'nameError': 'nameError', 'date': 'date'})
    writer.writerows(characters_list)

