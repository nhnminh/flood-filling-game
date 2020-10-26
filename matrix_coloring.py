import numpy as np
import copy

class Cell:
    def __init__(self, i, j, val):
        self.i = i
        self.j = j
        self.val = val
        self.visited = False
        
    def __repr__(self):
        # return "(" + str(self.i) + "," + str(self.j) + ": " + str(self.val) + ")"
        return str(self.val)

    def print(self):
        print(str(self.i) + "," + str(self.j) + ": " + str(self.val))  

    def printAll(self):
        print(str(self.i) + "," + str(self.j) + ": " + str(self.val) + " - visited = " + str(self.visited))  

    def toString(self):
        return "[" + str(self.i) + "," + str(self.j) + ": " + str(self.val) + "]"


class FloodFillingGame: 
    def __init__(self, nSize, mColor, type):
        if(type == 1):
            # if nSize is dimension
            self.matrix = np.array([[Cell(i, j, np.random.randint(0, mColor)) for j in range(nSize)] for i in range(nSize)])
            self.n = nSize
        else:
            # if nSize is a matrix
            self.matrix = np.array([[Cell(i, j, nSize[i][j]) for j in range(len(nSize))] for i in range(len(nSize))])
            self.n = len(nSize)

        self.m = mColor

    def getMatrix(self):
        return self.matrix

    def validCell(self, i, j, visited):
        if(i < self.n and i >= 0 and 
            j < self.n and j >=0 and 
            visited[i][j] == False) :
            return True
        else:
            return False

    
    def originGroup(self, matrix):

        queueBFS = []
        queueBFS.append(matrix[0][0])
        listOrigin = set({})
        listOrigin.add(matrix[0][0])
        visited = np.full((self.n, self.n), False)

        while(queueBFS):
            # print("-----------------------------")
            # print(queueBFS)

            #Pop 
            cur = queueBFS.pop()
            # print("Current cell: ")
            # cur.print()
            i = cur.i
            j = cur.j
            val = cur.val
            # print("current value = " + str(val))
            if(self.validCell(i, j+1, visited) and matrix[i][j+1].val == val):    
                queueBFS.append(matrix[i][j+1])
                listOrigin.add(matrix[i][j+1])
                # print("valid 1" + matrix[i][j+1].toString())
            if(self.validCell(i, j-1, visited) and matrix[i][j-1].val == val):    
                queueBFS.append(matrix[i][j-1])
                listOrigin.add(matrix[i][j-1])
                # print("valid 2" + matrix[i][j-1].toString())
            if(self.validCell(i+1, j, visited) and matrix[i+1][j].val == val):    
                queueBFS.append(matrix[i+1][j])
                listOrigin.add(matrix[i+1][j])
                # print("valid 3" + matrix[i+1][j].toString())
            if(self.validCell(i-1, j, visited) and matrix[i-1][j].val == val):    
                queueBFS.append(matrix[i-1][j])
                listOrigin.add(matrix[i-1][j])
                # print("valid 4" + matrix[i-1][j].toString())
            # print("Valid Adjacent cells of " + cur.toString())
            
            visited[cur.i][cur.j] = True

            # print(queueBFS)
            # print("listOrigin : " )
            # print(listOrigin)
            # print("** Original matrix ** ")
            # print(matrix)
            # print("*************** ")
            
        # print(listOrigin)
        # for cell in listOrigin:
        #     cell.printAll()
        return listOrigin
        
    

class Solution():
    def __init__(self, game):
        self.game = game 
    
    def checkMove(self, matrix, color):
        # make a copy to avoid side effect
        temp = copy.deepcopy(matrix)
        self.move(temp, color)
        newListOrigin = self.game.originGroup(temp)
        return(len(newListOrigin))

    def move(self, matrix, color):
        listOrigin = self.game.originGroup(matrix)
        # print(matrix)
        for cell in listOrigin:
            matrix[cell.i][cell.j].val = color
        return(matrix)

    def greedyMoves(self):
        widest = 0
        steps = 0
        chosen = 0
        # print("===========================")
        while(steps < 100 ):
            print("*** run : " + str(steps))
            # print("--------------------")
            widest = 0
            for color in range(self.game.m):
                val = self.checkMove(self.game.matrix, color)
                # print("color : " + str(color) + " | val =  "+ str(val))
                if(val > widest):       
                    widest = val
                    chosen = color
            print("widest = " + str(widest) + " vs " + str(self.game.n * self.game.n) + ", chosen = " + str(chosen))
            self.game.matrix = self.move(self.game.matrix, chosen)
            # print(self.game.matrix)
            
            if(widest >= self.game.n * self.game.n):
                break;
            val = 0
            steps=steps+1
        print("===========================")
        print(self.game.matrix)

def main():
    print(" ============   Flood Filling Game ! =========== ")
    
    # random generator
    myGame = FloodFillingGame(20, 4, 1)
    print(myGame.getMatrix())

    play = Solution(myGame)
    play.greedyMoves()

    # test 1 ----- 
    
    # a = [[1,1,2,1], [1,1,1,2], [1,0,0,0],[2,1,1,0]]
    # testMatrix = np.array(a)
    # myGame = FloodFillingGame(testMatrix, 3, 2)
    # print(myGame.getMatrix())

    # play = Solution(myGame)
    # play.greedyMoves()
    # print(testMatrix)


if __name__ == "__main__":
    main()