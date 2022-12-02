x, y = 0, 0
print(f"Начальная точка: ({x}, {y})")
route = input("Введите направление движения: ")
distance = float(input("Введите количество шагов: "))
if route.lower() == "вниз":
    y -= distance
    print(f"Текущее положение: ({x}, {y})")
elif route.lower() == "вверх":
    y += distance
    print(f"Текущее положение: ({x}, {y})")
elif route.lower() == "вправо":
    x += distance
    print(f"Текущее положение: ({x}, {y})")
elif route.lower() == "влево":
    x -= distance
    print(f"Текущее положение: ({x}, {y})")
else:
    print("Не знаю как туда попасть)))))")