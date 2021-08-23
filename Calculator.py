import math

class output:
  def __init__(output, a, b, c):
    output.a = a
    output.b = b
    output.c = c

def inputs(letters):

    alpha = ""
    beta = ""
    gamma = ""
    if string == 0:
      alpha = input("What is a?(input number)")
      if letters > 1:
         beta = input("What is b?(input number)")
         if letters > 2:
              gamma = input("What is c?(input number)")

    Output1 = output(alpha,beta,gamma)
    return Output1

letters = 1
string = 0
number_list_main = ("1","2","3","4","5")
number_list_trig = ("1","2","3","4","5","6")
number_list_pythagoras = ("1","2")
number_list_power = ("1","2","3","4")
number_list_function = ("1","2","3","4")
print("[1] Trigonometry\n[2] Pythagoras\n[3] Quadratic\n[4] Power_functions \n[5] +,-,*,/")

try:
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
                answer = math.sin(math.radians(float(Output1.a)))
            elif equation == "2":
                print("sin-1(a)")
                letters = 1
                string = 1
                alpha = inputs(letters)
                answer = math.asin(alpha)
            elif equation == "3":
                print("cos(a)")
                letters = 1
                output = inputs(letters)
                alpha = alpha(output)
                answer = math.cos(alpha)
            elif equation == "4":
                print("cos-1(a)")
                letters = 1
                output = inputs(letters)
                alpha = alpha(output)
                answer = math.acos(alpha)
            elif equation == "5":
                print("tan(a)")
                letters = 1
                output = inputs(letters)
                alpha = alpha(output)
                answer = math.tan(alpha)
            elif equation == "6":
                print("tan-1(a)")
                letters = 1
                output = inputs(letters)
                alpha = alpha(output)
                answer = math.atan(alpha)
      elif equation_set == "2":
         print("[1]a2+b2 \n[2]a2-b2")
         equation = input("What equation?(input number in bracket):")
         if equation in number_list_pythagoras:
            if equation == "1":
                print("a2 + b2")
            elif equation == "2":
                print("a2 - b2")
      elif equation_set == "3":
         print("(−b ± √(b2 − 4ac))/2a")
      elif equation_set == "4":
         print("[1]√a \n[2]a2 \n[3]a√b \n[4]ab9")
         equation = input("What equation?(input number in bracket):")
         if equation in number_list_power:
            if equation == "1":
               print("√a")
            elif equation == "2":
               print("a2")
            elif equation == "3":
               print("a√b")
            elif equation == "4":
               print("ab")
      elif equation_set == "5":
         print("[1]a+b \n[2]a-b \n[3]a*b \n[4]a/b")
         equation = input("What equation?(input number in bracket):")
         if equation in number_list_function:
            if equation == "1":
               print("a+b")
            elif equation == "2":
               print("a-b")
            elif equation == "3":
               print("a*b")
            elif equation == "4":
               print("a/b")
   print(answer)
except ValueError:
  print("Syntax error")
