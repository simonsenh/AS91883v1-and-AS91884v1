import math


# function prints each item in menu list and gets inputs and tests inputs
def run_menu(menu_list):
    i = 0
    menu_number = 1
    while i < len(menu_list):
        print('[' + str(i + 1) + '] ' + menu_list[i])
        i = i + 1
    y = False
    while y is False:
        menu_number = input("Select an option?(input number in square bracket):")
        y = test_int(menu_number)
        if y is True:
            if int(menu_number) < 1 or int(menu_number) > len(menu_list):
                y = False
    return int(menu_number) - 1


# creates a class to store up to 3 inputs a,b,& c
class Output:
    def __init__(Output, a, b, c):
        Output.a = a
        Output.b = b
        Output.c = c


# test if string is a int
def test_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


# test if string is a float
def test_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


# gets inputs for a,b,c depending on the variable letters which is 1,2, or 3
def inputs(letters):
    alpha = "0"
    beta = "0"
    gamma = "0"
    y = False
    while y is False:
        alpha = input("What is a?(input number):")
        y = test_float(alpha)
        if y is False:
            print("input a number!!!")
    if letters > "1":
        y = False
        while y is False:
            beta = input("What is b?(input number):")
            y = test_float(alpha)
            if y is False:
                print("input a number!!!")
        y = False
        if letters > "2":
            while y is False:
                gamma = input("What is c?(input number):")
                y = test_float(alpha)
                if y is False:
                    print("input a number!!!")
    output1 = Output(float(alpha), float(beta), float(gamma))
    return output1


# calculates answer based on equation name and outputs a b & c
def calcanswer(equation, output1):
    answer = 1
    if equation == "sin(a)":
        answer = math.sin(math.radians(output1.a))
    elif equation == "sin-1(a)":
        answer = math.asin(math.radians(output1.a))
    elif equation == "cos(a)":
        answer = math.cos(math.radians(output1.a))
    elif equation == "cos-1(a)":
        answer = math.acos(math.radians(output1.a))
    elif equation == "tan(a)":
        answer = math.tan(math.radians(output1.a))
    elif equation == "tan-1(a)":
        answer = math.atan(math.radians(output1.a))
    elif equation == "a ^ 2 + b ^ 2":
        answer = math.sqrt((output1.a ** 2) + output1.b ** 2)
    elif equation == "a ^ 2 - b ^ 2":
        answer = math.sqrt((output1.a ** 2) - output1.b ** 2)
    elif equation == "-b +- (((b ^ 2) - 4ac)/2a) ^ 1/2":
        a = output1.a
        b = output1.b
        c = output1.c
        x = ((b ** 2) - (4 * a * c))
        x = abs(x)
        x = math.sqrt(x)
        answer1 = (-b + x) / (2 * a)
        answer2 = (-b - x) / (2 * a)
        answer = str(answer1) + " and " + str(answer2)
    elif equation == "a ^ 2":
        answer = output1.a ** 2
    elif equation == "a ^ 1/2":
        answer = output1.a ** (1 / 2)
    elif equation == "a ^ b":
        answer = output1.a ** output1.b
    elif equation == "a ^ 1/b":
        answer = output1.a ** (1 / output1.b)
    elif equation == "a + b":
        answer = output1.a + output1.b
    elif equation == "a - b":
        answer = output1.a - output1.b
    elif equation == "a * b":
        answer = output1.a * output1.b
    elif equation == "a / b":
        answer = output1.a / output1.b
    return answer


# main menu
main_menu = ("Trigonometry", "Pythagoras", "Quadratic", "Power_functions", "+,-,*,/")
# 1 trig sub menu
trig_menu = ("sin(a)", "sin-1(a)", "cos(a)", "cos-1(a)", "tan(a)", "tan-1(a)")
trig_letters = ("1", "1", "1", "1", "1", "1")
# 2 pythag sub menu
pythag_menu = ("a ^ 2 + b ^ 2", "a ^ 2 - b ^ 2")
pythag_letters = ("2", "2")
# 3 quad option
quadratic_letters = "3"
# 4 power sub menu
power_menu = ("a ^ 2", "a ^ 1/2", "a ^ b", "a ^ 1/b")
power_letters = ("1", "1", "2", "2")
# epic sub menu
epic_menu = ("a + b", "a - b", "a * b", "a / b")
epic_letters = ("2", "2", "2", "2")


def main():
    equation = 1
    letters = 1
    repeat = "1"
    while repeat == "1":
        equation_set = run_menu(main_menu)
        if equation_set == 0:
            selection = run_menu(trig_menu)
            equation = trig_menu[selection]
            letters = trig_letters[selection]
        if equation_set == 1:
            selection = run_menu(pythag_menu)
            equation = pythag_menu[selection]
            letters = pythag_letters[selection]
        if equation_set == 2:
            equation = "-b +- (((b ^ 2) - 4ac)/2a) ^ 1/2"
            letters = quadratic_letters
        if equation_set == 3:
            selection = run_menu(power_menu)
            equation = power_menu[selection]
            letters = power_letters[selection]
        if equation_set == 4:
            selection = run_menu(epic_menu)
            equation = epic_menu[selection]
            letters = epic_letters[selection]
        print(equation)
        output1 = inputs(letters)
        answer = calcanswer(equation, output1)
        print("ANSWER: {}".format(answer))
        y = False
        while y is False:
            repeat = input("Do you want to log off?(1 for no, 2 for yes)")
            if repeat not in ("1", "2"):
                print("1 or 2")
            else:
                if repeat == "2":
                    print("thank you for using calculator by Henry Simonsen")
                y = True


main()

