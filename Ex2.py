a1 = float(input('Введите число:'))
a2 = float(input('Введите пограничное число: '))
if a1<a2:
    print("Перове число меньше пограничного")
if a1>a2:
    if (a1/a2 > 3):
        print("Первое число больше пограничного более, чем в 3 раза")
    else:
        print("Первое число больше пограничного")
