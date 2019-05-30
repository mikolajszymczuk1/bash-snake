# Simple snake text game in python.
from os import system
from time import sleep

class Board(object):
    """ This class make board width some width and height.  """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__board = []
        self.__draw()  # When board's size set then draw a board.

    def __str__(self):
        return "Board size : {0}x{1}".format(self.width, self.height)

    def __draw(self):
        """ Draw method who draws board game.  """

        for h in range(self.height):  # Make rows.
            row = []
            for w in range(self.width):  # Make columns.
                row.append(0)

            self.__board.append(row)  # Add row to board.

    def show(self):
        """ This method works as frame, show actual game state.  """

        for row in self.__board:
            print("|", end="")
            for column in row:
                if column == 0:
                    print("[ ]", end=" ")

                else:
                    print("[*]", end=" ")
            
            print("|\n")

    def get_element(self, row, col):
        """ Get elements from squeare with cords : [row, col]. """
        
        return self.__board[row - 1][col - 1]
    
    def set_element(self, row, col, val):
        """ Set value in squeare with cords : [row, col]. """

        self.__board[row - 1][col - 1] = val


# Test program.
mb = Board(10, 10)
while True:
    mb.show()
    sleep(0.1)
    system("clear")
