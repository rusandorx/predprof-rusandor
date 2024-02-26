import csv


def count_games(errors):
    '''
    Ф-ция, считающая количество ошибок для каждой игры
    :param errors: ошибки с одинаковыми играми, которые нужно посчитать
    :return: ошибки с новым полем "counter", в котором записано кол-во ошибок в этой игре
    '''

    # Создаем словарь где каждой игре соответсвует ее кол-во ошибок
    names = {name: 0 for name in set(map(lambda error: error['GameName'], errors))}
    for error in errors:
        # К кол-ву ошибок игры добавляем еще одну, найденную
        names[error['GameName']] += 1

    for error in errors:
        # Каждой ошибке добавляем поле 'counter' соответствующее кол-ву ошибок
        error['counter'] = names[error['GameName']]

    return errors


# Считываем файл через csv.DictReader
with open('game.txt', encoding='utf8') as file:
    reader = list(csv.DictReader(file, quotechar='"', delimiter='$'))

# Подсчитваем и сортируем ошибки
counted_errors = count_games(reader)
counted_errors.sort(key=lambda error: error['counter'])

# Создаем новый файл на основе ошибок с полем 'counter'
with open('game_counter.csv', 'w', newline='', encoding='utf8') as file:
    # Я не уверен, следует ли оставить разделитель "$", но я заменил на ","
    writer = csv.DictWriter(file, delimiter=',', quotechar='"',
                            fieldnames=['GameName', 'characters', 'nameError', 'date', 'counter'])
    writer.writeheader()
    writer.writerows(counted_errors)
