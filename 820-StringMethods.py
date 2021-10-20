def main():
    test = "Hello World!"
    print(test.upper())
    print(test.lower())

    answer = input()

    if answer.lower() == 'yes':
        print('okay')
    else:
        print('not ok')

if __name__ == '__main__':
    main()