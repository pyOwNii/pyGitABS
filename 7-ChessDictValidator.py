chessBoard = {
    "1a": "wrook",
    "2a": "wpawn",
    "6a": "bpawn",
    "8a": "brook",
    "2b": "wpawn",
    "5b": "bpawn",
    "1c": "wbishop",
    "2c": "wbishop",
    "3c": "wpawn",
    "6c": "bknight",
    "7c": "bpawn",
    "1d": "wqueen",
    "2d": "wknight",
    "5d": "bpawn",
    "8d": "bqueen",
    "6e": "bbishop",
    "7e": "bbishop",
    "1f": "wrook",
    "2f": "wpawn",
    "3f": "wknight",
    "6f": "bknight",
    "8f": "brook",
    "1g": "wking",
    "2g": "wpawn",
    "7g": "bpawn",
    "8g": "wking",  ##2 wkings here
    "2h": "wpawn",
    "7h": "bpawn",
}

def isValidChessBoard(board):
    blackPieces = 0
    whitePieces = 0
    pieces = ("king", "queen", "rook", "bishop", "knight", "pawn")

    boardPieces = list(board.values())

    #We check the kings, that IF black or white kings isnt 1 then its false:
    if boardPieces.count("bking") != 1 or boardPieces.count('wking') != 1:
        print(boardPieces.count("bking"))
        print(boardPieces.count("wking"))
        return False

    #We check the number of pawns we do not want more than 8 of each
    if boardPieces.count("bpawn") > 8 or boardPieces.count("wpawn") > 8:
        print(boardPieces.count("bpawn"))
        print(boardPieces.count("wpawn"))
        return False

    #Checking the number of pieces per color.
    for i in boardPieces:
        if i[0] == "b" and i[1:] in pieces:
            blackPieces += 1
        elif i[0] == "w" and i[1:] in pieces:
            whitePieces += 1
        else:
            return False

    #Checking the number of pieces for each color.
    if blackPieces > 16 or whitePieces > 16:
        print(blackPieces)
        print(whitePieces)
        return False

    #checking the spaces in the board.
    for spaces in board:
        if spaces[0] not in "12345678" or spaces[1] not in "abcdefgh":
            print("here")
            return False

    return True





def main():
    print(isValidChessBoard(chessBoard))


if __name__ == '__main__':
    main()