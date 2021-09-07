import math


# function prints each item in menu list and gets inputs and tests inputs
def run_menu(menu_list):
    # init variables 
    i = 0
    menu_number = 1
    # loop to go through each item in list and display with a [number] + list text
    while i < len(menu_list):
        print('[' + str(i + 1) + '] ' + menu_list[i])
        i = i + 1
    # y tells us if input is a good input
    y = False
    # loop to get valid input 
    while y is False:
        # gets menu item input from user
        menu_number = input("Select an option?(input number in square bracket):")
        # tests is an integer
        y = test_int(menu_number)
        # if integer tests if valid option on menu i.e between 1 & number in list
        if y is True:
            if int(menu_number) < 1 or int(menu_number) > len(menu_list):
                y = False
    # returns menu option selected
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
        # tries converting string to integer, if work return true
        int(string)
        return True
    # if fails return false
    except ValueError:
        return False


# test if string is a float
def test_float(string):
    try:
        # tries converting string to float, if work return true
        float(string)
        return True
    # if fails return false
    except ValueError:
        return False


# gets inputs for a,b,c depending on the variable letters which is 1,2, or 3
def inputs(letters):
    # sets all variables at 0
    alpha = "0"
    beta = "0"
    gamma = "0"
    y = False
    # loop until user inputs correct data type
    while y is False:
        alpha = input("What is a?(input number):")
        y = test_float(alpha)
        if y is False:
            print("input a number!!!")
    # If statment so it can get more variables if letters is more than one
    if letters > "1":
        y = False
        # loop until user inputs correct data type
        while y is False:
            beta = input("What is b?(input number):")
            y = test_float(alpha)
            if y is False:
                print("input a number!!!")
        # If statment so it can get more variables if letters is more than two
        y = False
        if letters > "2":
            # loop until user inputs correct data type
            while y is False:
                gamma = input("What is c?(input number):")
                y = test_float(alpha)
                if y is False:
                    print("input a number!!!")
    output1 = Output(float(alpha), float(beta), float(gamma))
    return output1


# calculates answer based on equation name and outputs a b & c
def calcanswer(equation, output1):
    # sets answer to one
    answer = 1
    # calculates answer based of output1 and equation
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
    #This equation is far more complex than the others so it needs 2 outputs and longer calculations
    elif equation == "-b +- (((b ^ 2) - 4ac)/2a) ^ 1/2":
        # converts variables into easy to type letters
        a = output1.a
        b = output1.b
        c = output1.c
        # dose top halve of the calculation
        x = ((b ** 2) - (4 * a * c))
        # square roots x even if negative
        x = abs(x)
        x = math.sqrt(x)
        # calculates two answer
        answer1 = (-b + x) / (2 * a)
        answer2 = (-b - x) / (2 * a)
        # makes answer equal both answers to print
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
# 5 epic sub menu
epic_menu = ("a + b", "a - b", "a * b", "a / b")
epic_letters = ("2", "2", "2", "2")


def main():
    # sets variables to 1
    equation = 1
    letters = 1
    repeat = "1"
    # loop calculation code until user wants to log off
    while repeat == "1":
        # gets input and prints the menu
        equation_set = run_menu(main_menu)
        #bassed off equation_set chooses what type of equation to process
        if equation_set == 0:
            # gathers and process and stores trig data in two variables
            selection = run_menu(trig_menu)
            equation = trig_menu[selection]
            letters = trig_letters[selection]
        if equation_set == 1:
            # gathers and process and stores pythag data in two variables
            selection = run_menu(pythag_menu)
            equation = pythag_menu[selection]
            letters = pythag_letters[selection]
        if equation_set == 2:
            # gathers and process and stores quadratic data in two variables
            equation = "-b +- (((b ^ 2) - 4ac)/2a) ^ 1/2"
            letters = quadratic_letters
        if equation_set == 3:
            # gathers and process and stores power data in two variables
            selection = run_menu(power_menu)
            equation = power_menu[selection]
            letters = power_letters[selection]
        if equation_set == 4:
            # gathers and process and stores epic data in two variables
            selection = run_menu(epic_menu)
            equation = epic_menu[selection]
            letters = epic_letters[selection]
        #prints equation then gets inputs for the equation and calculates
        print(equation)
        output1 = inputs(letters)
        answer = calcanswer(equation, output1)
        # displays answer
        print("ANSWER: {}".format(answer))
        # if user whats to log of or repeat it sets repeat to 2 or 1
        y = False
        # loop until input equals one or two
        while y is False:
            repeat = input("Do you want to log off?(1 for no, 2 for yes)")
            if repeat not in ("1", "2"):
                print("1 or 2")
            else:
                # if input is 2 the code will stop but if one it will loop to start
                if repeat == "2":
                    print("thank you for using calculator by Henry Simonsen")
                y = True


main()

