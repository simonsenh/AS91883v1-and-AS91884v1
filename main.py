import math
import random

computer_money = 100
your_money = 100
computer_bet = 0
your_bet = 5
add_bet = 0

cards_one = random.randint(1,13)
cards_two = random.randint(1,13)
cards_three = random.randint(1,13)
cards_four = random.randint(1,13)
cards_five = random.randint(1,13)
your_card_one = random.randint(1,13)
your_card_two = random.randint(1,13)
computer_card_one = random.randint(1,13)
computer_card_two = random.randint(1,13)

while your_bet > 0:
    print(your_card_one,your_card_two)
    computer_bet += 10
    print("The computers bet is {}".format(computer_bet))
    add_bet = int(input("What is your bet?"))
    your_bet += add_bet
    add_bet = 0
    if your_bet > computer_bet:
      computer_bet = your_bet
    if your_bet < computer_bet:
       print("The computer won{}".format(your_bet))
       computer_money += your_bet
       your_money -= your_bet
       computer_bet = 0
       your_bet = 0
    print("The computers bet is {}".format(computer_bet))
    print(cards_one,cards_two,cards_three)
    add_bet = int(input("What is your bet?"))
    your_bet += add_bet
    add_bet = 0
    if your_bet > computer_bet:
       computer_bet = your_bet
    if your_bet < computer_bet:
       print("The computer won {}".format(your_bet))
       computer_money += your_bet
       your_money -= your_bet
       computer_bet = 0
       your_bet = 0
    print("The computers bet is {}".format(computer_bet))
    print(cards_one,cards_two,cards_three,cards_four)
    add_bet = int(input("What is your bet?"))
    your_bet += add_bet
    add_bet = 0
    if your_bet > computer_bet:
        computer_bet = your_bet
    if your_bet < computer_bet:
       print("The computer won {}".format(your_bet))
       computer_money += your_bet
       your_money -= your_bet
       computer_bet = 0
       your_bet = 0
    print("The computers bet is {}".format(computer_bet))
    print(cards_one,cards_two,cards_three,cards_four,cards_five)
    add_bet = int(input("What is your bet?"))
    your_bet += add_bet
    add_bet = 0
    if your_bet > computer_bet:
       computer_bet = your_bet
    if your_bet < computer_bet:
       print("The computer won {}".format(your_bet))
       computer_money += your_bet
       your_money -= your_bet
       computer_bet = 0
       your_bet = 0
    print("The computers bet is {}".format(computer_bet))
