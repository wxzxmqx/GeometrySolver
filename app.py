
PI = 3.14159

def square():
    a = float(input(' Type the side length of the square: '))
    area = a ** 2
    print(f"\n The area of the square is: {area} square units.\n")
    return area

def rectangle():
    a = float(input(' Type the first length of the side of the rectangle: '))
    b = float(input(' Type the second length of the side of the rectangle: '))
    area = a * b
    print(f"\n The area of the rectangle is: {area} square units.\n")
    return area

def triangle():
    a = float(input(' Type the base of triangle: '))
    h = float(input(' Type the height of the triangle: '))
    area = (1 / 2) * a * h
    print(f"\n The area of the triangle is: {area} square units.\n")
    return area

def circle():
    r = float(input(' Type the radius of the circle: '))
    area = PI * (r ** 2)
    print(f"\n The area of the circle is: {area} square units.\n ")
    return area

def ellipse():
    a = float(input(' Type the semi-axe of the ellipse (Major): '))
    b = float(input(' Type the semi-axe of the ellipse (Minor): '))
    area = PI * a * b
    print(f"\n The area of the ellipse is: {area} square units.\n")
    return area

def trapezoid():
    a = float(input(' Type the length of the parallel side: '))
    b = float(input(' Type the length of the parallel side: '))
    h = float(input(' Type the height of trapezoid: '))
    area = 1 / 2 * (a + b) * h
    print(f"\n The area of the trapezoid is: {area} square units.\n")
    return area

def parallelogram():
    a = float(input(' Type the length of one side: '))
    h = float(input(' Type the height of parallelogram: '))
    area = a * h
    print(f"\n The area of the parallelogram is: {area} square units.\n")
    return area

def rhombus():
    d1 = float(input(' Type the first diagonal of the rhombus: '))
    d2 = float(input(' Type the second diagonal of the rhombus: '))
    area = (1 / 2) * d1 * d2
    print(f"\n The area of the rhombus is: {area} square units.\n")
    return area

def sphere():
    r = float(input(' Type the radius of the sphere: '))
    area = 4 * PI * (r ** 2)
    print(f"\n The surface area of the sphere is: {area} square units.\n")
    return area

def cylinder():
    r = float(input(' Type the radius of the base: '))
    h = float(input(' Type the height of cylinder: '))
    area = 2 * PI * r * h
    print(f"\n The lateral surface area of the cylinder is: {area} square units.\n")
    return area

'''Here is the greeting section'''
def greeting():
    print(" Welcome to the Friendly Area Calculator! 😊")
    print(" I will help you calculate the area of various shapes. Let's get started!")

def options():
    print('\n Available shapes:')
    print(' 1. Square')
    print(' 2. Rectangle')
    print(' 3. Triangle')
    print(' 4. Circle')
    print(' 5. Ellipse')
    print(' 6. Trapezoid')
    print(' 7. Parallelogram')
    print(' 8. Rhombus')
    print(' 9. Sphere')
    print(' 10. Cylinder')


    choice = int(input('\n Choose the option from 1 to 10: '))

    if choice == 1:
        square()
    elif choice == 2:
        rectangle()
    elif choice == 3:
        triangle()
    elif choice == 4:
        circle()
    elif choice == 5:
        ellipse()
    elif choice == 6:
        trapezoid()
    elif choice == 7:
        parallelogram()
    elif choice == 8:
        rhombus()
    elif choice == 9:
        sphere()
    elif choice == 10:
        cylinder()
    else:
        print(' Ugh, something went wrong. Re-check your option, please!')

quit = False
greeting()

while not quit:
    ask = input(f' Would you like to calculate? y/n: ').lower()
    if ask == "y":
        options()
    else:
        print(' Okay. Goodbye! \n')
        quit = True