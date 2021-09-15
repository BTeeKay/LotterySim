import cs50
import random


def main():

    num = []

    getnumbers(num)
    print("Thank you for entering your numbers")
    print("Let's see if you are lucky today")
    # Populate Winners list with random numbers, using getrandom function

    winners = []

    for i in range(len(num)):
        winners.append(getrandom())
    while isdup(winners) == True:
        winners.clear()
        for i in range(len(num)):
            winners.append(getrandom())

    #print(f"The Winning Numbers are: {winners}")


    #matching(winners, num)
    counter = 0
    while simulation(winners, num) < 6:
        counter += 1
        winners.clear()
        for j in range(len(num)):
            winners.append(getrandom())
        while isdup(winners) == True:
            winners.clear()
            for i in range(len(num)):
                winners.append(getrandom())
        simulation(winners, num)

    print(f"Your numbers took {counter} times to win!")


def simulation(winners, num):
    x = 0
    for j in range(len(winners)):
        if num[j] in winners:
            x += 1
    return x


def getnumbers(num):

    # Get int input from the user within a certain range
    for i in range(6):
        z = cs50.get_int(f"Number {i + 1}: ")
        while z < 0 or z > 59:
            z = cs50.get_int(f"Number {i + 1}: ")

        num.append(z)

    return num


def getrandom():

    # generate random number and return value
    x = random.randrange(1, 60)
    return x

def isdup(winners):

    dup = any(winners.count(x) > 1 for x in winners)
    return dup
    #while dup == True:
        #winners.clear()
        #for i in range(len(num)):
            #winners.append(getrandom())
        #dup = any(winners.count(x) > 1 for x in winners)





if __name__ == "__main__":
    main()
