import random, sys, os, math

def collatz(number):
    if number % 2 == 0:  #No rest = even.
        print(number // 2)
        return number // 2

    elif number % 2 == 1: #Rest = odd
        result = 3 * number + 1
        print(result)
        return result


def main():
    n = input("Give me a number: ")
    while n != 1:
        n = collatz(int(n))









#this is a script
if __name__ == '__main__':
    main()