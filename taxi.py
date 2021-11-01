# Основоной цикл программы
while True:
    # Ввод данных
    members = int(input('Введите кол-во сотрудников:'))
    rates = input('Введите тарифы такси:').split()
    if len(rates)!=members:
        print('Неверное количество аргументов!')
        continue
    rates_sorted = sorted([int(s) for s in rates])
    distances=input('Введите растояния до дома сотрудников:').split()
    if len(distances)!=members:
        print('Неверное количество аргументов!')
        continue
    distances_sorted = sorted([int(s) for s in distances], reverse=True)
    # Получение результата
    for member in range(members):
        current_index = distances_sorted.index(int(distances[member]))
        print(current_index + 1)
        distances[member] = 0
        distances_sorted[current_index] = 0
    # Диалог с пользователем
    while True:
        temp = int(input('Чтобы продолжить введите 0, чтобы выйте введите 1'))
        if temp==1:
            raise SystemExit
        elif temp==0:
            break
        else:
            print('Неверно введена команда, попробуйте снова')


