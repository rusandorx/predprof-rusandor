import csv



def binary_search(games, character):
    '''
    Реализация бинарного поиска персонажа по играм.
    :param games: игры по которым осуществляется поиск
    :param character: персонаж, которого нужно найти
    :return: игру c таким персонажем
    '''
    length = len(games)
    if length == 0 or length == 1 and character != games[0]['characters']:
        return None
    middle = length // 2

    # Персонаж найден
    if games[middle]['characters'] == character:
        return games[middle]

    # Персонаж в первой половине массива
    elif games[middle]['characters'] > character:
        return binary_search(games[0:middle], character)

    # Персонаж во второй половине массива
    return binary_search(games[middle+1:length], character)


with open('game.txt', encoding='utf8', newline='') as file:
    reader = list(csv.DictReader(file, delimiter='$', quotechar='"'))
    # Сортируем, чтобы работал бинарный поиск
    reader.sort(key=lambda x: x['characters'])

# Бесконечный цикл, пока не введено "game"
while (character := input('Введите имя персонажа:\t')) != 'game':
    # Копия массива, из которого будут удаляться найденные игры
    games_copy = reader.copy()
    first_res = binary_search(games_copy, character)
    if not first_res:
        print('Этого персонажа не существует')
        continue

    print(f'Персонаж {character} встречается в играх:')
    print(first_res['GameName'])
    # Удаление всех найденных игр и их дубликатов по названию.
    games_copy = list(filter(lambda game: game['GameName'] != first_res['GameName'], games_copy))
    for i in range(5):
        res = binary_search(games_copy, character)
        if not res:
            break
        elif i == 4:
            print('и др.')
            break
        print(res['GameName'])
        games_copy = list(filter(lambda game: game['GameName'] != res['GameName'], games_copy))


