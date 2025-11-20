"""This program converts Celsius Degrees in Fahrenheit Degrees"""

def converts_degree():
    try:
        celsius = int(input("Write your Celsius Degrees to convert: "))
        if celsius == int or float:
            farenheit = (celsius * 9 / 5) + 32
            print(f"It's equal to {farenheit} °F")
        else:
            raise ValueError("Degrees must be a number!")
    except ValueError:
        print("Degrees must be a number!")
        return

   
print("Welcome to my Celsius to Fahrenheit degrees converter!")

go_on = True

while go_on == True:

    converts_degree()
    
    x = input("Do you want to convert another number?(Y/n) ")
    if x == "n":
        print("Bye, see you soon!")
        go_on = False
