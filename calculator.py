print("Part 1")
def add (a, b, c, d, e, f, g, h, i, j):
    return a + b + c + d + e + f + g + h + i + j
def subtract (a, b, c, d, e, f, g, h, i, j):
    return a - b - c - d - e - f - g - h - i - j
def multiply (a, b, c, d, e, f, g, h, i, j):
    return a * b * c * d * e * f * g * h * i * j
def divide (a, b, c, d, e, f, g, h, i, j):
    return a / b / c / d / e / f / g / h / i / j
print(" ")
print ("Calculator")
print(" ")
print ("Select operation.")
print ("1. Add")
print ("2. Subtract")
print ("3. Multiply")
print ("4. Divide")
print(" ")
while True:
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        num4 = float(input("Enter fourth number: "))
        num5 = float(input("Enter fifth number: "))
        num6 = float(input("Enter sixth number: "))
        num7 = float(input("Enter seventh number: "))
        num8 = float(input("Enter eighth number: "))
        num9 = float(input("Enter nineth number: "))
        num10 = float(input("Enter tenth number: "))
        print(" ")
        if choice == '1':
            print(num1,"+", num2,"+", num3,"+", num4,"+", num5,"+", num6,"+", num7,"+", num8,"+", num9,"+", num10,"=", add(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10))
        elif choice == '2':
            print(num1,"-", num2,"-", num3,"-", num4,"-", num5,"-", num6,"-", num7,"-", num8,"-", num9,"-", num10,"=", subtract(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10))
        elif choice == '3':
            print(num1,"×", num2,"×", num3,"×", num4,"×", num5,"×", num6,"×", num7,"×", num8,"×", num9,"×", num10,"=", multiply(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10))
        elif choice == '4':
            print(num1,"÷", num2,"÷", num3,"÷", num4,"÷", num5,"÷", num6,"÷", num7,"÷", num8,"÷", num9,"÷", num10,"=", divide(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10))
        print(" ")
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            print(" ")
            print ('If you need more help I am glad to help you, till then cya.')
            print(" ")
            break
        elif next_calculation == "yes":
            print(" ")
            print("Ok then let's see, which do you want to do now?\n 1.Add \n2. Subtract\n3. Multiply\n4. Divide")
            print(" ")
            continue
        else:
            print("Invalid Input")
            print(" ")
            break
    else:
        print("Invalid input")
        break