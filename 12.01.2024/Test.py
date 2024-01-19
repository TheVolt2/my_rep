import pandas as pd
article = pd.read_csv('data.csv', delimiter = ';', names = ['top_game', 'fail_game', 'my_games', 'phone_games', 'random_id'])
print(article)

def rename_data():
    a = int(input('Введите координату 1 чтобы её изменить(начиная с 0): '))
    b = int(input('Введите координату 2 чтобы её изменить(начиная с 0): '))
    rename = input('Введите значение:')
    article.iloc[a, b] = rename
    article.to_csv("data.csv", index=False, sep=";")

def search_data():
    koordinata_1 = int(input('Введите координату 1 чтобы её найти(начиная с 0): '))
    koordinata_2 = input('Введите название столбика чтобы его найти(top_game, fail_game, my_games, phone_games, random_id): ')
    print(article.at[koordinata_1, koordinata_2])

func = int(input('Введите номер функции(что она делает пойми из названия, data это название документа со столбцами) из 1 - rename_data, 2 - search_data: '))

if func == 1:
    print(rename_data())

elif func == 2:
    print(search_data())

print(article)
