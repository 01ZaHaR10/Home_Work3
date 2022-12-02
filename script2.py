x, y = 0, 0
print(f"Начальная точка: ({x}, {y})")
print(f'Если хотите прекратить движение введите - "остановиться"')
while True:
    route = input("Введите направление движения: ")
    if route.lower() == "остановиться":
        print(f"Конечное положение: ({x}, {y})")
        break
    else:
        distance = float(input("Введите количество шагов: "))
        if distance < 0:
            print("Не знаю как пройти по этому пути(((")
        elif route.lower() == "вниз":
            y -= distance
        elif route.lower() == "вверх":
            y += distance
        elif route.lower() == "вправо":
            x += distance
        elif route.lower() == "влево":
            x -= distance
        else:
            print("Не знаю как туда попасть(((")
        print(f"Текущее положение: ({x}, {y})")