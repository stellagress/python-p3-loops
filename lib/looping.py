#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i >= 0:
        print(i)
        i -= 1
    print('Happy New Year!')

        # for i in range(10):
        # i -= 1
        # if i == 0:
        #     print("Happy New Year!")


def square_integers(int_list):
    return [i ** 2 for i in int_list]
        





def fizzbuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
             print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

