def main():
    test = "Hello World!"
    print(test.upper())
    print(test.lower())

    #answer = input()

    # if answer.lower() == 'yes':
    #     print('okay')
    # else:
    #     print('not ok')
    #

    print(test.islower())

    print("hello".upper().isupper())

    #.isalpha ## letters
    #.isalnum() ## letters and numerics
    #.isdecimal()
    #.isspace()

    #.istitle() #title

    print("hello world!".startswith("hello"))
    print("hello world".endswith("world"))

    #join
    print(', '.join(['cats', 'rats', 'bats']))
    print(''.join(['cats', 'rats', 'bats']))
    print(' '.join(['cats', 'rats', 'bats']))
    print('\n'.join(['cats', 'rats', 'bats']))

    #split
    print("my name is hello".split())
    print("my name is hello".split("m"))

    #ljust rjust
    print("hello".rjust(10))
    print("hello".ljust(10))
    print("hello".rjust(20, "*"))
    print("hello".center(20, "="))

    name = 'Test'
    print(name.center(20, '"'))

    #strip to remove

    spam = "aaaarrraaaarrraaaa"
    print(spam.strip("aaaa"))   #removes the other aaaas

    #replace
    spamx = 'Hello there'
    print(spamx.replace('e', 'XYZ'))

if __name__ == '__main__':
    main()