import math


"""This program calculate Area & Perimeter of 2D geometric objects"""


class Triangle():
    def __init__(self, cateto_1, cateto_2, ipotenusa):
        self.cateto_1 = cateto_1
        self.cateto_2 = cateto_2
        self.ipotenusa = ipotenusa

    def is_triangle(self):
        if (self.cateto_1 + self.cateto_2 > self.ipotenusa
            and self.cateto_1 + self.ipotenusa > self.cateto_2
            and self.cateto_2 + self.ipotenusa > self.cateto_1
        ):
            return True
        else:
            return False
        
    def calculate_perimeter(self):
        perimeter = (self.cateto_1 + self.cateto_2 + self.ipotenusa)
        return perimeter
    

    def calculate_area(self):
        semiperimeter = self.calculate_perimeter() / 2
        area = (math.sqrt(semiperimeter*(semiperimeter-self.cateto_1)
                *(semiperimeter - self.cateto_2)
                *(semiperimeter - self.ipotenusa))
        )
        print(f"The area of this Triangle is: {area}")
        

class Square():
    def __init__(self, base):
        self.base = base
    
    def calculate_perimeter(self):
        perimeter = self.base * 4
        print(f"The Perimeter of thic Square is: {perimeter}")

    def calculate_area(self):
        area = self.base**2
        print(f"The Area of this Square is: {area}")


class Rectangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_area(self):
        area = self.base * self.height
        print(f"The Area of this Rectangle is: {area}")

    def calculate_perimeter(self):
        perimeter = (self.base + self.height) * 2
        print(f"The Perimeter of this Rectangle is: {perimeter}")



go_on = True

print("Welcome to the Perimeter & Area Calculator")

while go_on == True:
    print("-------------     Menù    -------------")
    print("--  Select the corresponding number  --")
    print(" ")
    print("1. Triangle")
    print("2. Square")
    print("3. Rectangle")
    print(" ")
    object = int(input("Choose an object: "))
    match object:
        case 1:
            print("You choose Triangle!")
            try:
                side_1 = float(input("Insert the first side: "))
                side_2 = float(input("Insert the second side: "))
                side_3 = float(input("Insert the third side: "))
            except ValueError:
                print("You entered an invalid value")
                continue

            triangle = Triangle(side_1, side_2, side_3)
            valid = triangle.is_triangle()
            if valid == True:
                print("What you want to calculate? ")
                print("1. Perimeter")
                print("2. Area")
                print("3. Both")

                try:
                    selection = int(input("Select: "))
                except ValueError:
                    print("Invalid selection")
                    continue

                match selection:    
                    case 1:
                        perimeter = triangle.calculate_perimeter()
                        print(f"The perimeter of this Triangle is: {perimeter}")
                        input("press enter to continue..")
                    case 2:
                        triangle.calculate_area()
                        input("press enter to continue..")
                    case 3:
                        perimeter = triangle.calculate_perimeter()
                        print(f"The perimeter of this Triangle is: {perimeter}")
                        triangle.calculate_area()
                        input("press enter to continue..")
            else:
                print("This is not a triangle")
                continue
        
        case 2:
            print("You choose Square!")
            try:
                side = float(input("Insert the side: "))
            except ValueError:
                print("You entered an invalid value!")
                continue

            square = Square(side)

            print("What you want to calculate? ")
            print("1. Perimeter")
            print("2. Area")
            print("3. Both")

            try:
                selection = int(input("Select: "))
            except ValueError:
                print("Invalid selection")
                continue

            match selection:    
                case 1:
                    square.calculate_perimeter()
                    input("press enter to continue..")
                case 2:
                    square.calculate_area()
                    input("press enter to continue..")
                case 3:
                    square.calculate_perimeter()
                    square.calculate_area()
                    input("press enter to continue..")
        case 3:
            print("You choose Rectangle!")
            try:
                base = float(input("Insert the base: "))
                height = float(input("Insert the height: "))
            except ValueError:
                print("You entered an invalid value")
                continue

            rectangle = Rectangle(base, height)

            print("What you want to calculate? ")
            print("1. Perimeter")
            print("2. Area")
            print("3. Both")
            try:
                selection = int(input("Select: "))
            except ValueError:
                print("Invalid selection")
                continue

            match selection:    
                case 1:
                    rectangle.calculate_perimeter()
                    input("press enter to continue..")
                case 2:
                    rectangle.calculate_area()
                    input("press enter to continue..")
                case 3:
                    rectangle.calculate_perimeter()
                    rectangle.calculate_area()
                    input("press enter to continue..")

    x = input("Do you want to continue?(Y/n) ")   
    if x in ["n", " n", "n ", "N", " N", "N "]:
        print("Bye, see you soon!")
        go_on = False
    else:
        continue             
                            
