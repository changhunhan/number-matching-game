import random

rd = random.randint(1,100)

while True:
    try:
        rd_input = int(input())

        if rd_input > rd: print("down")
        elif rd_input < rd: print("up")
        elif rd_input == rd:
            print("great!")
            break
    except:
        print("You must input integer")
