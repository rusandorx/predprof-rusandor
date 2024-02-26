import csv

with open('game.txt', encoding='utf8') as file:
    reader = csv.DictReader(file, quotechar='"', delimiter='$')
    rows, fieldnames = list(reader), reader.fieldnames
    new_rows = []
    for row in rows:
        if '55' in row['nameError']:
            print(
                f'У персонажа\t{row['characters']}\tв игре\t{row['GameName']}\tнашлась ошибка с кодом:\t '
                f'{row['nameError']}.\tДата фиксации:\t {row['date']}')
            row['nameError'] = 'Done'
            row['date'] = '0000-00-00'
        new_rows.append(row)

with open('game_new.csv', 'w', encoding='utf8', newline='') as file:
    # Я не уверен, следует ли оставить разделитель "$", но я заменил на ","
    writer = csv.DictWriter(file, delimiter=',', quotechar='"', fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(new_rows)
