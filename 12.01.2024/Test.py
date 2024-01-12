import pandas as pd
aricle = pd.read_csv('data.csv', delimiter = ';', names = ['top_game', 'fail_game', 'my_games', 'phone_games'])

a = int(input('Введите координату 1(начиная с 0):'))
b = int(input('Введите координату 2(начиная с 0):'))
rename = input('Введите значение:')

aricle.iloc[a, b] = rename
aricle.to_csv("data.csv", index=False, sep=";")
print(aricle)