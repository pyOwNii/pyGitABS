#list is a value that contains multiple values in ordered sequence
#can be called items in the list
#remember array from c++

def main():
    x = ['a','b','c','d','e']
    print(x[1])
    print(x[2])

    y = [['a','b'] , [10,20,30,40,50]]
    print(y[0][0])      #accesses first item in the first list

    ##Slices
    print(x[1:3])   #does not include the value at 3.


    z = [10,20,30]
    z[1] = 'Hello'
    print(z)

    del x[2]
    print(x)

    print(len([1,2,3]))

    print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])


# this is a script
if __name__ == '__main__':
    main()