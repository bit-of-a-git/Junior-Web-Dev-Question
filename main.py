import time

for number in range(1, 100):
    if number % 2 == 0 and number % 3 == 0:
        print("ab")
    elif number % 2 == 0:
        print("a")
    elif number % 3 == 0:
        print("b")
    else:
        print(str(number))
    time.sleep(.5)
