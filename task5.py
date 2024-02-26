import csv
import string


def generate_hash(s: str):
    '''
    Генерирует хэш на основе строки.
    :param s: Строка которую нужно хешировать
    :return: Результат хеш-функции
    '''

    # Каждому символу даем нужное значение в соответствии с условием
    # В условии указано: "1 → 53 … 0 → 63, : → 64, - → 65." но последовательно 0 не может быть = 63:
    # 1 - 53, 2 - 54, 3 - 55, 4 - 56, 5 - 57, 6 - 58, 7 - 59, 8 - 60, 9 - 61, 0 - 62 !!!!
    # К тому же в названиях игр есть "'", о чем ничено не сказано в условии.
    # Так что я решил сделать так:
    # 1 - 53, 2 - 54, 3 - 55, 4 - 56, 5 - 57, 6 - 58, 7 - 59, 8 - 60, 9 - 61, ' - 62, 0 - 63
    alp = {char: i for i, char in
           enumerate(string.ascii_lowercase + string.ascii_uppercase + string.digits[1:] + "'0" + ':' + '-', 1)}

    # Инициируем переменные данные в формуле хеш-функции
    m = 10 ** 9 + 9
    p = 65
    p_pow = 0
    hash = 0

    for char in s:
        hash += (hash + alp[char] * p ** p_pow) % m
        p_pow += 1

    return hash


def get_hash_input(error):
    '''
    Получить значение названия игры + имя персонажа без пробелов
    :param error: Ошибка по которой нужно получить значение аргумента для хеш-функции
    :return: Название игры + имя перснонажа без пробелов
    '''
    # Я увидел, что у одной игры есть "." в названии. Об этом ничего не сказано в условии.
    # Так что я ее просто проигнорирую?
    return error['GameName'].replace(' ', '').replace('.', '') + error['characters']


# Считываем файл через csv.DictReader
with open('game.txt', encoding='utf8') as file:
    reader = list(csv.DictReader(file, quotechar='"', delimiter='$'))

# Для каждой ошибки создаем хеш
for error in reader:
    hash_input = get_hash_input(error)
    error['hash'] = generate_hash(hash_input)

# Записываем в новый файл с хешом
with open('game_with_hash.csv', 'w', newline='', encoding='utf8') as file:
    # Я вновь до конца не знаю, следует ли менять разделитель. Но поменял его на запятую
    writer = csv.DictWriter(file, quotechar='"', delimiter=',',
                            fieldnames=['hash', 'GameName', 'characters', 'nameError', 'date'])
    writer.writeheader()
    writer.writerows(reader)
