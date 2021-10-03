import random


def main():
    numberOfStreaks = 0

    for experimentNumber in range(10000):
        # code that creates a list of 100 'heads or tails' values.

        flipList = []   # Creates a new empty list for the 100 values to be added here.
        for i in range(100):
            flipList.append(random.randint(0, 1))
                        # filling the list with 0s and 1s

                        # code that checks if there is a streak of 6 heads or tails in row
        streak = 1       # we always start with 1 because any toss automatically becomes 1.
        for i in range(1, len(flipList)):   # we start from position 2 since we will look back.
            if flipList[i] == flipList[i-1]:    # check if current list item is the same as before
                streak += 1
            else:
                streak = 1  # we restart with 1.

            if streak == 6:
                numberOfStreaks += 1
                break

    print('Chance of streak: %s%%' % (numberOfStreaks / 100))


if __name__ == '__main__':
    main()
