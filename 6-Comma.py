def comma(ourList):
    if len(ourList) == 1:
        print(ourList[0])
    else:
        for item in ourList:
            if item != ourList[-1]:
                print(item + ', ', end='')
            else:
                print('and ' + ourList[-1])



def main():
    spam = ['apples', 'bananas', 'tofu', 'cats']
    comma(spam)



if __name__ == '__main__':
    main()