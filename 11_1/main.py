import pandas as pd
df = pd.read_csv("california_housing_test.csv")

# # | Задача 40: Определить среднюю стоимость дома,
# # где кол-во людей от 0 до 500 (population)
print(f"Средняя стоимость дома при популяции населения от 0 до 500:\n\
    {df[(df['population'] > 0) & (df['population'] <500)]['median_house_value'].mean()}")
print()
# # | Задача 42: Узнать какая максимальная households в зоне
# # минимального значения population |
print(f"Количество членов семьи в зоне с минимальной популяцией:\n\
    {df[df['population']==df['population'].min()]['households'].max()}")