import math
import random

print("y")

x = 2

def math(x):
    return x + 3

print(math(x))

input = 1

def inputs(input):
    alpha = input("What is a?(input number)")
    if inputs > 1:
        beta = input("What is b?(input number)")
        if inputs > 2:
            delta = input("What is c?(input number)")
            if inputs > 3:
                gamma = input("What is d?(input number)")
                alpha = alpha * 1000000000000000
                beta = beta * 1000000000
                delta = delta * 100000
                return alpha + beta + delta + gamma

def alpha(output):
   round(output)
def beta(output):

def gamma(output):

def delta(output):


main_equations = ("trigonometry_(1)","pythagoras_(2)","Quadratic_(3)","power_functions_(4)","+,-,*,/_(5)")
trig_equations = ("sin(a)_(1)","sin-1(a)_(2)","cos(a)_(3)","cos(a)-1_(4)","tan(a)_(5)","tan(a)_(6)")
pythagoras_equations = ("a2+b2_(1)","a2-b2_(2)")
power_equations = ("√a_(1)","a2_(2)","a√b_(3)","ab_(4)")
function_equations = ("a+b_(1)","a-b_(2)","a*b_(3)","a/b_(4)")
number_list_main = ("1","2","3","4","5")
number_list_trig = ("1","2","3","4","5","6")
number_list_pythagoras = ("1","2")
number_list_power = ("1","2","3","4")
number_list_function = ("1","2","3","4")
print(main_equations)
try:
   equation_set = input("What equation set?(input number in bracket)")
   if equation_set in number_list_main:
      if equation_set == 1:
         print(trig_equations)
         equation = input("What equation?(input number in bracket)")
         if equation in number_list_trig:
            if equation == 1:
                print("sin(a)")
            if equation == 2:
                print("sin-1(a)")
            if equation == 3:
                print("cos(a)")
            if equation == 4:
                print("cos(a)-1")
            if equation == 5:
                print("tan(a)")
            if equation == 6:
                print("tan(a)-1")
      elif equation_set == 2:
         print(pythagoras_equations)
         equation = input("What equation?(input number in bracket)")
         if equation in number_list_pythagoras:
            if equation == 1:
               print("a2 + b2")
            if equation == 2:
               print("a2 - b2")
      elif equation_set == 3:
         print("(−b ± √(b2 − 4ac))/2a")
      elif equation_set == 4:
         print(power_equations)
         equation = input("What equation?(input number in bracket)")
         if equation in number_list_power:
            if equation == 1:
               print("√a")
            if equation == 2:
              print("a2")
            if equation == 3:
              print("a√b")
            if equation == 4:
              print("ab")
      elif equation_set == 5:
         print(function_equations)
         equation = input("What equation?(input number in bracket)")
         if equation in number_list_function:
            if equation == 1:
              print("a+b")
            elif equation == 2:
              print("a-b")
            elif equation == 3:
              print("a*b")
            elif equation == 4:
              print("a/b")

except ValueError:
  print("Syntax error")
