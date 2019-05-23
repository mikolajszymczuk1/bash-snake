# Simple snake text game in python.

class MakeBoard(object):
    """ This class make board width some width and height.  """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "Board size : {0}x{1}".format(self.width, self.height)


myBoard = MakeBoard(100, 200)
print(myBoard)
