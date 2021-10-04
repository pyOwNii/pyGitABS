import pprint

def main():
    # myCat = {
    #     'size' : 'fat',
    #     'color': 'gray',
    #     'disposition' : 'loud'
    # }
    #
    # print(myCat['size'])
    # y = 'My cat has ' + myCat['color'] + ' fur.'
    # print(y)
    #
    # spam = {
    #     12345: 'Luggage combination',
    #     42: 'The Answer'
    # }
    # ## does not have an order just like list
    #
    # print(12345 in spam)
    # print(spam)
    #
    # print(spam.keys())
    # print(spam.items())
    #
    # for k in spam.keys():
    #     print(k)        ## OR THE VALUES
    #
    # for k, v in spam.items():
    #     print(k,v)
    #
    # #TUPLES ARE IMMUTABLE BUT ARE LIKE LIST WRITTEN WITH PARANTHESES
    #
    # if 12345 in spam:
    #     print(spam[12345])
    #
    # #get method
    # print(spam.get(12345, 0))
    # print(spam.get(123457, 'DOES NOT EXIST IN DICT'))
    #
    # #set def method
    # spam.setdefault('color', 'black')
    # print(spam)

    message = 'It was a birght cold day in April, and the clocks were striking thirteen.'
    count = {

    }   #'r' : 12

    for character in message.upper():
        count.setdefault(character, 0) # start of with 0
        count[character] = count[character] + 1

    print(count)
    pprint.pprint(count)    #PRETTY PRINT
    print('\n')

    rjtext = pprint.pformat(count)  #PFORMAT TO RETURN A STRING VALUE
    print(rjtext)



if __name__ == '__main__':
    main()
