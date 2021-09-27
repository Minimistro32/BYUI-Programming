'''
Author: Tyson Freeze
Assignment: Tic-Tac-Toe (Week 2)
Class: CSE 210
Notes: Everything but the diagonal win condition, works for any gameboard size with width and height >= 2. 
    I ran out of time to program  a diagonal win condition for a rectangular gameboard.
    Hitting enter when asked for user input will cause the game to crash.
'''

class TicTacToe:
    # init
    def __init__(self, width=3, height=None) -> None:  # rectangular boards and square boards
        # init fields
        board = []
        self.width = 2 if width < 2 else width
        if height is None:
            self.height = width
        else:
            self.height = 2 if height < 2 else height
        self.roundCounter = 1
        self.isPlaying = True

        # init board
        squareCounter = 0
        for y in range(0, self.height):
            board.append([])
            for x in range(0, self.width):
                squareCounter += 1
                board[y].append(Square(squareCounter))

        self.board = board
        print('\nWelcome to Tic, Tac, Toe!\n')


    # print functions
    def printBoard(self):
        isBigBoard = self.width * self.height > 9
        for y in range(0, self.height):
            for x in range(0, self.width):  # print Numbers
                thisSquare = self.board[y][x]

                extraSpacerChar = " " if isBigBoard and (
                    thisSquare.hasBeenPlayed() or (self.width * y) + (x + 1) < 10) else ""
                columnSeperator = " | " if x != self.width - 1 else ""

                print(extraSpacerChar + thisSquare.getColor() + thisSquare.getValue() +
                      thisSquare.endColor() + columnSeperator, end="")

            # print rowSeperator
            if y != self.height - 1:
                rowSeperator = ""
                seperatorTile = "  - +" if isBigBoard else " - +"
                for i in range(0, self.width - 1):
                    rowSeperator += seperatorTile
                print("\n" + rowSeperator[1:] + seperatorTile[:-2])
        print("\n", end="")

    def printGameOver(self, msg):
        print("\n\n" + msg)
        self.printBoard()
        print("Thanks for playing!\n")
        self.isPlaying = False

    # game logic
    def play(self):
        while self.isPlaying:
            print(
                f"\nRound {self.roundCounter} ({self.getCurrentPlayer()}'s Turn):")
            self.printBoard()
            selectedPosition = self.getValidInput()
            self.updateBoard(selectedPosition)

            if self.didWin(selectedPosition):
                self.printGameOver(
                    "\033[4m" + f"Good job, {self.getCurrentPlayer()}! You WON!!!" + "\033[0m")
            elif self.roundCounter == self.width * self.height:
                self.printGameOver(
                    "\033[4m" + "Sorry, looks like it's cat's game 😔." + "\033[0m")
            else:
                self.roundCounter += 1

    def updateBoard(self, position):
        charToPlace = self.getCurrentPlayer()
        self.getSquareByPos(position).setValue(charToPlace)

    # helper functions
    def getCurrentPlayer(self):
        return 'X' if self.roundCounter % 2 == 1 else 'O'

    def getValidInput(self, msg="Pick a number to play: "): # Will still crash if the user simply hits 'enter', but so does the solution. I could not figure this out.
        while True:
            try:
                response = int(input(msg))
            except ValueError:
                msg = "Please enter a number: "

            if response > self.width * self.height or response < 1:
                msg = "Please pick a number on the board: "
            elif self.getSquareByPos(response).hasBeenPlayed() == True:
                msg = "Please pick a new number to play: "
            else:
                return response

    def getSquareByPos(self, position): # figured it out with math, you don't need a loop :D
        position -= 1
        xPos = int(position % self.width)
        yPos = int((position - (position % self.width)) / self.width)
        return self.board[yPos][xPos]

    # win condition helper functions. (I think the three checkSquare functions could be reduce to 1 function by using vector components in an array.)
    def didWin(self, position):
        position -= 1
        xPos = int(position % self.width)
        yPos = int((position - (position % self.width)) / self.width)
        return self.checkSquareInRow(yPos, xPos) or self.checkSquareInCol(yPos, xPos) or self.checkSquareInDiag(yPos, xPos)

    def checkSquareInRow(self, yPos, xPos, xPrev=None):
        if self.board[yPos][xPos].getValue() == self.getCurrentPlayer():
            if xPos != 0 and xPos != self.width - 1 and xPrev is None:
                return self.checkSquareInRow(yPos, xPos - 1, xPos) and self.checkSquareInRow(yPos, xPos + 1, xPos)
            elif xPos != 0 and (xPrev is None or xPos < xPrev): # (not at the end) and ((starting recursion) or (headed down the array already))
                return self.checkSquareInRow(yPos, xPos - 1, xPos) # continue going left down the array
            elif xPos != self.width - 1 and (xPrev is None or xPos > xPrev): # (not at the end) and ((starting recursion) or (headed down the array already))
                return self.checkSquareInRow(yPos, xPos + 1, xPos) # continue going right down the array
            else:
                return True  # we've traversed to the end of the row, either left or right
        else:
            return False

    def checkSquareInCol(self, yPos, xPos, yPrev=None):
        if self.board[yPos][xPos].getValue() == self.getCurrentPlayer():
            if yPos != 0 and yPos != self.height - 1 and yPrev is None:
                return self.checkSquareInCol(yPos - 1, xPos, yPos) and self.checkSquareInCol(yPos + 1, xPos, yPos)
            elif yPos != 0 and (yPrev is None or yPos < yPrev):
                return self.checkSquareInCol(yPos - 1, xPos, yPos)
            elif yPos != self.height - 1 and (yPrev is None or yPos > yPrev):
                return self.checkSquareInCol(yPos + 1, xPos, yPos)
            else:
                return True
        else:
            return False

    def checkSquareInDiag(self, yPos, xPos, vector=None): #assumes a grid
        if self.board[yPos][xPos].getValue() == self.getCurrentPlayer() and (yPos == xPos or (self.height - yPos - 1) == xPos): #is (correct 'X' or 'O') and (on a diag)
            if vector is None:
                if yPos == xPos and (self.height - yPos - 1) == xPos: #start on the center
                    return (self.checkSquareInDiag(yPos - 1, xPos - 1, [-1, -1]) and self.checkSquareInDiag(yPos + 1, xPos + 1, [1, 1])) or (self.checkSquareInDiag(yPos + 1, xPos - 1, [1, -1]) and self.checkSquareInDiag(yPos - 1, xPos + 1, [-1, 1]))
                elif xPos != 0 and xPos != self.width - 1: #starting in a middle square
                    if yPos == xPos:
                        vector1 = [-1, -1]
                        vector2 = [1, 1]
                    elif (self.height - yPos - 1) == xPos:
                        vector1 = [1, -1]
                        vector2 = [-1, 1]
                    return self.checkSquareInDiag(yPos + vector1[0], xPos + vector1[1], vector1) and self.checkSquareInDiag(yPos + vector2[0], xPos + vector2[1], vector2)
                elif xPos != 0: #starting left
                    if yPos == xPos: 
                        vector = [-1, -1]
                    elif (self.height - yPos - 1) == xPos: 
                        vector = [1, -1]
                    return self.checkSquareInDiag(yPos + vector[0], xPos + vector[1], vector)
                else: #starting right
                    vector = [1, 1] if yPos == xPos else [-1, 1]
                    return self.checkSquareInDiag(yPos + vector[0], xPos + vector[1], vector)
            else:
                if xPos != 0 or xPos != self.width - 1: #reached an end
                    return True
                else:
                    return self.checkSquareInDiag(yPos + vector[0], xPos + vector[1], vector) #keep going
        else:
            return False


class Square:
    def __init__(self, initialValue):
        self.value = str(initialValue)
        self.canBePlayed = True

    def getColor(self):
        if self.value == "X":
            return "\033[1;31m"  # bold red
        elif self.value == "O":
            return "\033[1;34m"  # bold blue
        else:
            return "\033[37m"  # white

    def hasBeenPlayed(self):
        return not(self.canBePlayed)

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue
        if self.value != 'X' or self.value != 'O':
            self.canBePlayed = False

    def endColor(self):
        return '\033[0m'  # end color sequence


def main():
    twoByFour = TicTacToe(3)
    twoByFour.play()


if __name__ == "__main__":
    main()