UNIT_TO_METER = {
    "km": 1000,
    "m": 1,
    "cm": 0.01,
    "mm": 0.001,
    "inches": 0.0254
}

WEIGHT_TO_GRAMS = {
    "kg": 1000,        
    "g": 1,            
    "mg": 0.001,       
    "lbs": 453.59237,  
    "oz": 28.3495231   
}


class Conversion:
    def __init__(self, unit_1, unit_2, value):
        self.unit_1 = unit_1
        self.unit_2 = unit_2
        self.value = value

    def length_converter(self):
        value_in_meters = self.value * UNIT_TO_METER[self.unit_1]
        result = value_in_meters / UNIT_TO_METER[self.unit_2]
        print(f"The conversion from {self.unit_1} to {self.unit_2} is: {result}")
    
    def weight_converter(self):
        value_in_grams = self.value * WEIGHT_TO_GRAMS[self.unit_1]
        result = value_in_grams / WEIGHT_TO_GRAMS[self.unit_2]
        print(f"The conversion from {self.unit_1} to {self.unit_2} is: {result}")


go_on = True

print("Welcome to the Universal Converter")
while go_on == True:
    print("Menù")
    print("1. Convert Lengths")
    print("2. Convert Weights")
    try: 
        selection = int(input("Select: "))
    except ValueError:
        print("Selection not valid")
        continue
    match selection:
        case 1:
            print("You choose Lengths")
            print("Valid units: km | m | cm | mm | inches ")
            unit_1 = input("Choose the initial unit: ")
            unit_2 = input("Choose the result unit: ")
            try:
                if unit_1 in ["km", "m", "cm", "mm", "inches"]  and unit_2 in ["km", "m", "cm", "mm", "inches"]:
                    try:
                        value = float(input(f"Insert a value in {unit_1}: "))
                        result = Conversion(unit_1, unit_2, value)
                        result.length_converter()
                        input("Press enter to continue")
                        continue
                    except ValueError:
                        print("You didn't insert a number")
                else:
                    raise ValueError
            except ValueError:
                print("Invalid units")
                continue
        case 2:
            print("You choose Weights")
            print("Valid units: kg | g | mg | lbs | oz ")
            unit_1 = input("Choose the initial unit: ")
            unit_2 = input("Choose the result unit: ")
            try:
                if unit_1 in ["kg", "g", "mg", "lbs", "oz"] and unit_2 in ["kg", "g", "mg", "lbs", "oz"]:
                    try:
                        value = float(input(f"Insert a value in {unit_1}: "))
                        result = Conversion(unit_1, unit_2, value)
                        result.weight_converter()
                        input("Press enter to continue")
                        continue
                    except ValueError:
                        print("You didn't insert a number")
                else:
                    raise ValueError
            except ValueError:
                print("Invalid units")
                continue
            

    x = input("Do you want to continue?(Y/n) ")
    if x == "n" or " n" or "n " or "N":
        print("Bye, see you soon!")
        go_on = False
    else:
        continue

        
