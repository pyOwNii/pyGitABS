def main():
    # using double " quotes makes it that u can use single quotes in it.
    print("Hi")
    print('Say hi to bo\'s test\n')

    print('hello there.\nhow are u?\ntest')

    #raw string
    print(r'Hello')
    print(r'That is a cat')

    print(""" Test,
    test two
    tree
    
    leaves
    house""")

    testlength = """ Test,
    test two
    tree
    
    leaves
    house"""

    print(len(testlength))

    print(testlength[0:6])

if __name__ == '__main__':
    main()