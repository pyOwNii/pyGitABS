import pprint

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['bot-L'] + '|' + board['bot-M'] + '|' + board['bot-R'])

def main():
    cat = {
        'name': 'Zophie',
        'age': 7,
        'color': 'gray'
    }

    allCats = []
    allCats.append(
        {'name': 'Zophie',
        'age': 7,
        'color': 'gray'
    })

    allCats.append(
    {
        'name': 'Pooka',
        'age': 5,
        'color': 'black'
    })

    allCats.append(
    {
        'name': 'ABC',
        'age': 5,
        'color': 'gray'
    })

    allCats.append(
    {
        'name': '???',
        'age': -1,
        'color': 'orange'
    })

    print(allCats)

    theBoard = {
        'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
        'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
        'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '
    }

    pprint.pprint(theBoard)

    theBoard['mid-M'] = 'X'

    pprint.pprint(theBoard)
    theBoard['top-L'] = 'O'
    theBoard['top-M'] = 'O'
    theBoard['top-R'] = 'O'
    theBoard['mid-L'] = 'X'
    theBoard['bot-R'] = 'X'

    pprint.pprint(theBoard)

    printBoard(theBoard)

    print(type(42))
    print(type('hello'))
    print(type(3.14))
    print(type(theBoard))
    print(type(theBoard['top-R']))

    allGuests = {
        'Alice': {
            'apples': 5,
            'pretzels': 12
        },
        'Bob': {
            'ham sandwiches': 3,
            'apples': 2
        },
        'Carol': {
            'cups': 3,
            'apple pies': 1
        }
    }

    print('Number of things being brought:')
    print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
    print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
    print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
    print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
    print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))


def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought


## this "defines the script" also makes it look like a c++ structure which is "good"

if __name__ == '__main__':
    main()