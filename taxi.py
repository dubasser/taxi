members = int(input('Введите кол-во сотрудников:'))
rates = input('Введите тарифы такси:').split()
rates_sorted = sorted([int(s) for s in rates])
distances=input('Введите растояния до дома сотрудников:').split()
distances_sorted = sorted([int(s) for s in distances], reverse=True)
for member in range(members):
    current_index = distances_sorted.index(int(distances[member]))
    print(current_index+1)
    distances[member]=0
    distances_sorted[current_index]=0
