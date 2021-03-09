#test for myself

import stdio
import stdarray
import random
import os
class mineGrid:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.PercMine = 0
        
        self.array = stdarray.create2D(row, column , 0)
        self.front = stdarray.create2D(row, column , "?")
        stdarray.write2D(self.front)

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

    def printmineGrid(self):
        stdarray.write2D(self.array)

    def printGameGrid(self):
        stdarray.write2D(self.front)

    def checkBoundries(self, row, column):
        if row >= 0 and row < self.row and column >= 0 and column < self.column:
            return True
        return False
            

    def getCellValue(self, row, column):
        if self.checkBoundries(row, column) and self.front[row][column] == "?":
            return self.array[row][column]
        
        
        return -1

    def openCell(self, row, column):
        print(" openCell")
        cellVal = self.getCellValue(row, column)
        if cellVal == -1 or cellVal == "M":
            return
        
        if cellVal == 'X':
            print("you lost")
            self.front = self.array
            return 400


        if cellVal == 0:
            self.front[row][column] = self.array[row][column]
            for i in range(row - 1 , row + 2):
                for j in range(column - 1 , column + 2):
                    
                    if not (i == row and j == column): 
                        self.openCell(i, j)
        else:
            self.front[row][column] = self.array[row][column]

    def setMine(self, row, column):
        print(" setMine")
        if self.checkBoundries(row, column) and self.front[row][column] == "?":
            self.front[row][column] = "M"

    def checkCell(self, row, column):
        print(" checkCell")
        if self.checkBoundries(row, column) and self.front[row][column] == "?":
            #something\
            return
    def funcSwitcher(self, command, row, column):
        switcher={
                1: lambda: self.openCell( row -1, column-1),
                2: lambda: self.setMine( row -1, column-1),
                3: lambda: self.checkCell( row -1, column-1),
                }
        return switcher.get(command)()

def _main():
    """
    For testing.
    """
    
    grid = mineGrid(5, 4)
    grid.createMines(20)


    grid.printmineGrid()
    print("play, [1/2/3 - open, flag] [row] [columb]: [-1 to exit]")
    com, row, col = map(int, input().split())
    while (com != -1):
        res = grid.funcSwitcher(com, row, col)

        #os.system('cls')
        grid.printGameGrid()
        if (res == 400): break
        
        
        com, row, col = map(int, input().split())
    

if __name__ == '__main__':
    _main()