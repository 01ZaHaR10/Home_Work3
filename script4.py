import cmath
print("Введите коэффициенты для уравнения:")
print("ax^2 + bx + c = 0:")
a = complex(input("a = "))
b = complex(input("b = "))
c = complex(input("c = "))

if a.imag == 0 and b.imag == 0 and c.imag == 0:
    a, b, c = float(a.real), float(b.real), float(c.real)     
    discr = b ** 2 - 4 * a * c
    print("Дискриминант D = %.2f" % discr)
 
    if discr > 0:
        x1 = (-b + discr**0.5) / (2 * a)
        x2 = (-b - discr**0.5) / (2 * a)
        print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif discr == 0:
        x = -b / (2 * a)
        print("x = %.2f" % x)
    else:
        x1 = (-b + cmath.sqrt(discr)) / (2 * a)
        x2 = (-b - cmath.sqrt(discr)) / (2 * a)
        print(f"x1 = {x1} \nx2 = {x2}")
else:
    discr = b ** 2 - 4 * a * c
    print(f"Дискриминант D = {discr}" )
    if discr == 0:
        x = -b / (2 * a)
        print(f"x = {x}")
    else:
        x1 = (-b + cmath.sqrt(discr)) / (2 * a)
        x2 = (-b - cmath.sqrt(discr)) / (2 * a)
        print(f"x1 = {x1} \nx2 = {x2}")