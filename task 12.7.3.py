per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0} # словарь {ключ : значение, ... : ...}
money = float(input("Введите сумму вклада: ")) # ввод с клавиатуры
deposit = []
for x in list(per_cent.values()): # сисок значений словаря
    deposit.append(float(money * x / 100)) # вычисляем % от вклада
deposit = [round(x, 2) for x in deposit] # округление результата до 2х знаков
print(deposit) # вывод результатов
print(max(deposit)) # вывод максимального
