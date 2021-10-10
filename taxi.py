members = int(input('Введите кол-во сотрудников:'))
rates=input('Введите тарифы такси:').split()
rates_sorted = sorted([int(s) for s in rates])
distances=input('Введите растояния до дома сотрудников:').split()
distances_sorted = sorted([int(s) for s in distances], reverse=True)
for member in range(members):
    print('Сотрудник '+str(distances_sorted[member])+'км до дома садится в машину с тарифом '+str(rates_sorted[member])+' руб/км')
