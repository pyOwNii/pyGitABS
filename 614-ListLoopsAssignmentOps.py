def main():
    for i in range(4):
        print(i)

    print(range(4)) #0,1,2,3

    print(list(range(0, 100, 2)))

    supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
    for i in range(len(supplies)):
        print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

    supplies = ['pens','pens','pens','pens','pens','pens','pens']
    for i in range(len(supplies)):
        print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

    # size, color, dispositon = supplies
    # this assigns supplies0 to size, supples1 to color and supples2 to disposition
    # size,color,dispositon = '3', 'black', 'silent' another example.


    #augmented assignment operators

    e = 42
    e = e + 1
    e += 1
    print(e)

    


# this is a script
if __name__ == '__main__':
    main()