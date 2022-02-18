from random import random


def flip_coin():
    number = int(input("Number of times to flip coin: "))  # taking the input from the user
    heads = 0  # taking the head value is 0
    tails = 0  # taking the tail value is 0
    for i in range(number):
        coin = random()  # taking random number and that number stored in coin variable
    if coin < 0.5:  # checking the condition
        heads += 1
        print("Heads")
        headPercentage = (heads / number) * 100
        print("Head Percentage is : ", headPercentage)
    else:
        tails += 1
        print("Tails")
        tailPercentage = (tails / number) * 100
        print("Tail Percentage is : ", tailPercentage)
flip_coin()
