import math


# creates a class to store up to 3 inputs a,b,& c
class output:
    def __init__(output, a, b, c):
        output.a = a
        output.b = b
        output.c = c


def test_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def inputs(letters):
    alpha = "0"
    beta = "0"
    gamma = "0"
    y = False
    if string == 0:
        while y == False:
            alpha = input("What is a?(input number)")
            y = test_number(alpha)
            if y == False:
                print("input a number!!!")
        if letters > 1:
            y = False
            while y == False:
                beta = input("What is b?(input number)")
                y = test_number(alpha)
                if y == False:
                    print("input a number!!!")
            y = False
            if letters > 2:
                while y == False:
                    gamma = input("What is c?(input number)")
                    y = test_number(alpha)
                    if y == False:
                        print("input a number!!!")

    Output1 = output(float(alpha), float(beta), float(gamma))
    return Output1


letters = 1
string = 0
repeat = 1
number_list_main = ("1", "2", "3", "4", "5")
number_list_trig = ("1", "2", "3", "4", "5", "6")
number_list_pythagoras = ("1", "2")
number_list_power = ("1", "2", "3", "4")
number_list_function = ("1", "2", "3", "4")

while repeat == 1:
  print("[1] Trigonometry\n[2] Pythagoras\n[3] Quadratic\n[4] Power_functions \n[5] +,-,*,/")
  equation_set = input("What equation set?(input number in square bracket):")
  if equation_set in number_list_main:
      if equation_set == "1":
          print("[1] sin(a) \n[2] sin-1(a) \n[3] cos(a) \n[4] cos-1(a) \n[5] tan(a) \n[6] tan-1(a)")
          equation = input("What equation?(input number in bracket):")
          if equation in number_list_trig:
              if equation == "1":
                  print("sin(a)")
                  Letters = 1
                  Output1 = inputs(letters)
                  answer = math.sin(math.radians(Output1.a))
              elif equation == "2":
                  print("sin-1(a)")
                  letters = 1
                  Output1 = inputs(letters)
                  answer = math.asin(math.radians(Output1.a))
              elif equation == "3":
                  print("cos(a)")
                  letters = 1
                  Output1 = inputs(letters)
                  answer = math.cos(math.radians(Output1.a))
              elif equation == "4":
                  print("cos-1(a)")
                  letters = 1
                  Output1 = inputs(letters)
                  answer = math.acos(math.radians(Output1.a))
              elif equation == "5":
                  print("tan(a)")
                  letters = 1
                  Output1 = inputs(letters)
                  answer = math.tan(math.radians(Output1.a))
              elif equation == "6":
                  print("tan-1(a)")
                  letters = 1
                  Output1 = inputs(letters)
                  answer = math.atan(math.radians(Output1.a))
      elif equation_set == "2":
          print("[1]a^2+b^2 \n[2]a^2-b^2")
          equation = input("What equation?(input number in bracket):")
          if equation in number_list_pythagoras:
              if equation == "1":
                  print("a^2 + b^2")
                  letters = 2
                  Output1 = inputs(letters)
                  answer = math.sqrt((Output1.a ** 2) + (Output1.b) ** 2)
              elif equation == "2":
                  print("a^2 - b^2")
                  letters = 2
                  Output1 = inputs(letters)
                  answer = math.sqrt((Output1.a ** 2) - (Output1.b ** 2))
      elif equation_set == "3":
          print("(−b ± √(b^2 − 4ac))/2a")
          letters = 3
          Output1 = inputs(letters)
          a = Output1.a
          b = Output1.b
          c = Output1.c
          x = ((b ** 2) - (4 * a * c)) / (2 * a)
          x = x * x
          x = x / x
          x = math.sqrt(x)
          b = -b / (2 * a)
          answer = str(b + x) + " and " + str(b - x)
      elif equation_set == "4":
          print("[1]√a \n[2]a^2 \n[3]a√b \n[4]ab9")
          equation = input("What equation?(input number in bracket):")
          if equation in number_list_power:
              if equation == "1":
                  print("√a")
                  letters = 1
                  Output1 = inputs(letters)
                  answer = math.sqrt(Output1.a)
              elif equation == "2":
                  print("a^2")
                  letters = 1
                  Output1 = inputs(letters)
                  answer = Output1.a ** 2
              elif equation == "3":
                  print("a√b")
                  letters = 2
                  Output1 = inputs(letters)
                  answer = Output1.a ** (1 / Output1.b)
              elif equation == "4":
                  print("a^b")
                  letters = 2
                  Output1 = inputs(letters)
                  answer = Output1.a ** Output1.b
      elif equation_set == "5":
          print("[1]a+b \n[2]a-b \n[3]a*b \n[4]a/b")
          equation = input("What equation?(input number in bracket):")
          if equation in number_list_function:
              if equation == "1":
                  print("a+b")
                  letters = 2
                  Output1 = inputs(letters)
                  answer = Output1.a + Output1.b
              elif equation == "2":
                  print("a-b")
                  letters = 2
                  Output1 = inputs(letters)
                  answer = Output1.a - Output1.b
              elif equation == "3":
                  print("a*b")
                  letters = 2
                  Output1 = inputs(letters)
                  answer = Output1.a * Output1.b
              elif equation == "4":
                  print("a/b")
                  letters = 2
                  Output1 = inputs(letters)
                  answer = Output1.a / Output1.b
  print(answer)
  y = False
  while y == False:
    repeat = int(input("Do you want to log off?(1 for no, 2 for yes)"))
    if repeat != 1 or 2:
        y = False
        print("1 or 2")
    y = True
