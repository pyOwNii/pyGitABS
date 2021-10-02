def main():
    #method is same thing as a function but it is called as a valuue

    pam = ['hello', 'hi', 'howdy', 'heyas']
    print(pam.index('hello'))

    x = ['e','f','g','e']
    print(x.index('e'))

    x.append('a')     #adds at the end of the list
    print(x)

    #insert
    x.insert(1, 'newIndex')
    print(x)

    y = ['a', 'b', 'c']
    y.remove('a')       ##specifices what to delete no matter where in the list
    print(y)

    x.sort()
    print(x)

    #methods are functions that are called on values

if __name__ == '__main__':
    main()