import cs50
import random


def main():

    num = []

    getnumbers(num)
    print("Thank you for entering your numbers")
    print("Let's see if you are lucky today")
    winners = []
    for i in range(len(num)):
        winners.append(getrandom())
    print(f"The Winning Numbers are: {winners}")

    x = 0
    for j in range(len(winners)):
        if winners[j] == num[j]:
            print(f"Number {winners[j]} is a winner!")
            x += 1

    print(f"You got {x} matches")

def getnumbers(num):


    for i in range(6):
        z = cs50.get_int(f"Number {i + 1}: ")
        while z < 0 or z > 4:
            z = cs50.get_int(f"Number {i + 1}: ")


        num.append(z)

    return num


def getrandom():

    x = random.randrange(1,3)
    return x


if __name__ == "__main__":
    main()
