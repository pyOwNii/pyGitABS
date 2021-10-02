# def div42by(divideby):
#     try:
#         return 42 / divideby
#     except ZeroDivisionError:    #so this is like try and catch in c++
#         print('Error: You tried to divide by zero')


def main():
    # print(div42by(2))
    # print(div42by(12))
    # print(div42by(0))
    # print(div42by(1))
    print('How many do u have')
    number = input()
    try:
        if int(number) >= 4:
            print('Thats alot')
        else:
            print('Not so much')
    except ValueError:
        print('You didnt enter a number')
    ## input validation so that the program doesnt crash








#this is a script
if __name__ == '__main__':
    main()