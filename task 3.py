import csv

with open('game.txt', 'r', encoding='UTF-8') as file:
    characters_list = list(csv.DictReader(file, delimiter='$'))
    gamecount = {}
    for s in characters_list:
        if s['GameName'] not in gamecount:
            gamecount[s['GameName']] = 1
        else:
            gamecount[s['GameName']] += 1
    for s in characters_list:
        s['counter'] = gamecount[s['GameName']]

            
with open('game_counter.csv', 'w', encoding='UTF-8') as file:
    writer = csv.DictWriter(f=file, fieldnames=['GameName', 'characters', 'nameError', 'date', 'counter'], delimiter='$')
    writer.writerow({'GameName': 'GameName', 'characters': 'characters', 'nameError': 'nameError', 'date': 'date', 'counter' : 'counter'})
    writer.writerows(characters_list)
