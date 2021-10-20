
def main():
    #using double " quotes makes it that u can use single quotes in it.
    xyz = 'hello ' + 'world'
    name = 'Alice'
    place = 'Main Street'
    time = '6 pm'
    food = 'turnips'

    sentence = 'Hello ' + name + ', you are invited to a party at ' + place + ' at ' + time + '. Please ' + food + '.'
    print(sentence)

    sentence2 = 'Hello %s, your are invite to a party at %s at %s. Please bring %s.' %(name, place, time, food)
    print(sentence2)

if __name__ == '__main__':
    main()