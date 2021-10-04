

def main():
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]

    # we have 6 columns
    # and 9 rows

    print(grid[0])   #  6 columns
    print(len(grid)) # 9 rows

    columns = len(grid[0])
    rows = len(grid)

    for i in range(columns):        #basically we "rotate" it.
        for j in range(rows):
            print(grid[j][i], end='')
        print('')


   


if __name__ == '__main__':
    main()