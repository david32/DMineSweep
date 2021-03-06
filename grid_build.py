#test for myself

import stdio
import stdarray
import random

class mineGrid:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.PercMine = 0
        
        self.array = stdarray.create2D(row, column , 0)

    def createMines(self, percentage):

        self.PercMine = int(percentage)

        count = int(self.row * self.column * (self.PercMine/100))

        while count > 0:
            row = random.randint(0,self.row - 1)
            column = random.randint(0,self.column - 1)

            #print("row: " , row , "column: " ,  column)
            if (self.array[row][column] != 'X'):
                self.array[row][column] = 'X'
                count -= 1

                #update all the neighboring cells
                if (row != 0):
                    if (self.array[row-1][column] != 'X'):
                        self.array[row-1][column] = self.array[row-1][column] + 1
                    if (column != 0 and self.array[row-1][column - 1] != 'X'):
                        self.array[row-1][column - 1] = self.array[row-1][column - 1] + 1
                    if (column != self.column - 1 and self.array[row-1][column + 1] != 'X'):
                        self.array[row-1][column + 1] = self.array[row-1][column + 1] + 1

                if (column != 0 and self.array[row][column - 1] != 'X'):
                    self.array[row][column - 1] = self.array[row][column - 1] + 1
                if (column != self.column - 1 and self.array[row][column + 1] != 'X'):
                    self.array[row][column + 1] = self.array[row][column + 1] + 1

                #stdarray.write2D(self.array)

                if (row != self.row - 1):
                    if (self.array[row+1][column] != 'X'):
                        self.array[row+1][column] = self.array[row+1][column] + 1
                    if (column != 0 and self.array[row+1][column - 1] != 'X'):
                        self.array[row+1][column - 1] = self.array[row+1][column - 1] + 1
                    if (column != self.column - 1 and self.array[row+1][column + 1] != 'X'):
                        self.array[row+1][column + 1] = self.array[row+1][column + 1] + 1
            #stdarray.write2D(self.array)

    def printGrid(self):
        stdarray.write2D(self.array)


def _main():
    """
    For testing.
    """
    grid = mineGrid(5, 4)
    grid.createMines(20)

    grid.printGrid()

if __name__ == '__main__':
    _main()