import copy
import cv2
import time

from numpy import true_divide
GRID_SIZE = 3

Face1 = [["N" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
Face2 = [["N" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
Face3 = [["N" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
Face4 = [["N" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
Face5 = [["N" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
Face6 = [["N" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]



FaceExample = [
    ["N","N","N"],
    ["N","N","N"],
    ["N","N","N"]
]


class CubeOBJ:
    def __init__(self):

        #Faces#
        self.Face1 = copy.deepcopy(Face1)
        self.Face2 = copy.deepcopy(Face2)
        self.Face3 = copy.deepcopy(Face3)
        self.Face4 = copy.deepcopy(Face4)
        self.Face5 = copy.deepcopy(Face5)
        self.Face6 = copy.deepcopy(Face6)
        
        #Info
        self.Moves = []
        self.Solved = False

    def PrintFaces(self):

        print("Face 1:")
        for row1 in self.Face1:
            print(row1)
        print("Face 2:")
        for row1 in self.Face2:
            print(row1)
        print("Face 3:")
        for row1 in self.Face3:
            print(row1)
        print("Face 4:")
        for row1 in self.Face4:
            print(row1)
        print("Face 5:")
        for row1 in self.Face5:
            print(row1)
        print("Face 6:")
        for row1 in self.Face6:
            print(row1)

    def Move(self, Movement, FrontFaceNum=1):
        
        MoveNames = [  #NOT A 2D LIST JUST ORDED TO MATCH PAIRS
            "R","Ri", #0,1
            "L","Li", #2,3
            "B","Bi", #4,5
            "D","Di", #6,7
            "F","Fi", #8,9
            "U","Ui", #10,11
            "M", #12
        ]

        Face1 = self.Face1
        Face2 = self.Face2
        Face3 = self.Face3
        Face4 = self.Face4
        Face5 = self.Face5
        Face6 = self.Face6

        if FrontFaceNum == 2:
            Face1 = self.Face2
            Face2 = self.Face3
            Face3 = self.Face4
            Face4 = self.Face1

            MoveNames[0] = "B"
            MoveNames[1] = "Bi"
            MoveNames[2] = "F"
            MoveNames[3] = "Fi"
            MoveNames[4] = "L"
            MoveNames[5] = "Li"
            MoveNames[8] = "R"
            MoveNames[9] = "Ri"
            
        elif FrontFaceNum == 3:
            Face1 = self.Face3
            Face2 = self.Face4
            Face3 = self.Face1
            Face4 = self.Face2

            MoveNames[0] = "L"
            MoveNames[1] = "Li"
            MoveNames[2] = "R"
            MoveNames[3] = "Ri"
            MoveNames[4] = "F"
            MoveNames[5] = "Fi"
            MoveNames[8] = "B"
            MoveNames[9] = "Bi"

        elif FrontFaceNum == 4:
            Face1 = self.Face4
            Face2 = self.Face1
            Face3 = self.Face2
            Face4 = self.Face3

            MoveNames[0] = "F"
            MoveNames[1] = "Fi"
            MoveNames[2] = "B"
            MoveNames[3] = "Bi"
            MoveNames[4] = "R"
            MoveNames[5] = "Ri"
            MoveNames[8] = "L"
            MoveNames[9] = "Li"

        elif FrontFaceNum == 5: # modifes 5 and 6 
            Face1 = self.Face5
            Face2 = self.Face2
            Face3 = self.Face6
            Face4 = self.Face4
            Face5 = self.Face3
            Face6 = self.Face1

            MoveNames[4] = "D"
            MoveNames[5] = "Di"
            MoveNames[6] = "F"
            MoveNames[7] = "Fi"
            MoveNames[8] = "U"
            MoveNames[9] = "Ui"
            MoveNames[10] = "B"
            MoveNames[11] = "Bi"

        elif FrontFaceNum == 6: # modifes 5 and 6 
            Face1 = self.Face6
            Face2 = self.Face2
            Face3 = self.Face5
            Face4 = self.Face4
            Face5 = self.Face1
            Face6 = self.Face3

            MoveNames[4] = "U"
            MoveNames[5] = "Ui"
            MoveNames[6] = "B"
            MoveNames[7] = "Bi"
            MoveNames[8] = "D"
            MoveNames[9] = "Di"
            MoveNames[10] = "F"
            MoveNames[11] = "Fi"

        Face1Copy = copy.deepcopy(Face1) #add .self to 4revert 
        Face2Copy = copy.deepcopy(Face2)
        Face3Copy = copy.deepcopy(Face3)
        Face4Copy = copy.deepcopy(Face4)
        Face5Copy = copy.deepcopy(Face5)
        Face6Copy = copy.deepcopy(Face6)

        if Movement == "R": #right up* ("R")
            self.Moves.append(MoveNames[0])
            for i in range(GRID_SIZE):
                Face1[i][2] = Face6Copy[i][2]#
                Face5[i][2] = Face1Copy[i][2]#

            Face6[0][2] = Face3Copy[2][0]#
            Face6[1][2] = Face3Copy[1][0]#
            Face6[2][2] = Face3Copy[0][0]#

            Face3[0][0] = Face5Copy[2][2]#
            Face3[1][0] = Face5Copy[1][2]#
            Face3[2][0] = Face5Copy[0][2]#

            ###rotate face clockwise 
            Face2[0][0] = Face2Copy[2][0]
            Face2[0][1] = Face2Copy[1][0]
            Face2[0][2] = Face2Copy[0][0]
            Face2[1][2] = Face2Copy[0][1]
            Face2[2][2] = Face2Copy[0][2]
            Face2[2][1] = Face2Copy[1][2]
            Face2[2][0] = Face2Copy[2][2]
            Face2[1][0] = Face2Copy[2][1]
  
        elif Movement == "Ri": #right down* ("Ri")
            self.Moves.append(MoveNames[1])
            for i in range(GRID_SIZE):
                Face1[i][2] = Face5Copy[i][2]#
                Face6[i][2] = Face1Copy[i][2]#

            Face5[0][2] = Face3Copy[2][0]#
            Face5[1][2] = Face3Copy[1][0]#
            Face5[2][2] = Face3Copy[0][0]#

            Face3[0][0] = Face6Copy[2][2]#
            Face3[1][0] = Face6Copy[1][2]#
            Face3[2][0] = Face6Copy[0][2]#

            ###rotate face anti-clockwise 
            Face2[0][0] = Face2Copy[0][2]
            Face2[0][1] = Face2Copy[1][2]
            Face2[0][2] = Face2Copy[2][2]
            Face2[1][2] = Face2Copy[2][1]
            Face2[2][2] = Face2Copy[2][0]
            Face2[2][1] = Face2Copy[1][0]
            Face2[2][0] = Face2Copy[0][0]
            Face2[1][0] = Face2Copy[0][1]

        elif Movement == "L": #left down* ("L")
            self.Moves.append(MoveNames[2])
            for i in range(GRID_SIZE):
                Face1[i][0] = Face5Copy[i][0]#
                Face6[i][0] = Face1Copy[i][0]#

            Face3[0][2] = Face6Copy[2][0]#
            Face3[1][2] = Face6Copy[1][0]#
            Face3[2][2] = Face6Copy[0][0]#

            Face5[0][0] = Face3Copy[2][2]#
            Face5[1][0] = Face3Copy[1][2]#
            Face5[2][0] = Face3Copy[0][2]#

            ###rotate face clockwise 
            Face4[0][0] = Face4Copy[2][0]
            Face4[0][1] = Face4Copy[1][0]
            Face4[0][2] = Face4Copy[0][0]
            Face4[1][2] = Face4Copy[0][1]
            Face4[2][2] = Face4Copy[0][2]
            Face4[2][1] = Face4Copy[1][2]
            Face4[2][0] = Face4Copy[2][2]
            Face4[1][0] = Face4Copy[2][1]

        elif Movement == "Li": #left up* ("Li")
            self.Moves.append(MoveNames[3])
            for i in range(GRID_SIZE):
                Face1[i][0] = Face6Copy[i][0]#
                Face5[i][0] = Face1Copy[i][0]#

            Face6[0][0] = Face3Copy[2][2]#
            Face6[1][0] = Face3Copy[1][2]#
            Face6[2][0] = Face3Copy[0][2]#

            Face3[0][2] = Face5Copy[2][0]#
            Face3[1][2] = Face5Copy[1][0]#
            Face3[2][2] = Face5Copy[0][0]#

            ###rotate face anti-clockwise 
            Face4[0][0] = Face4Copy[0][2]
            Face4[0][1] = Face4Copy[1][2]
            Face4[0][2] = Face4Copy[2][2]
            Face4[1][2] = Face4Copy[2][1]
            Face4[2][2] = Face4Copy[2][0]
            Face4[2][1] = Face4Copy[1][0]
            Face4[2][0] = Face4Copy[0][0]
            Face4[1][0] = Face4Copy[0][1]

        elif Movement == "B": #back face to left  ("B")
            self.Moves.append(MoveNames[4])

            Face5[0][0] = Face2Copy[0][2]#
            Face5[0][1] = Face2Copy[1][2]#
            Face5[0][2] = Face2Copy[2][2]#

            Face6[2][0] = Face4Copy[0][0]#
            Face6[2][1] = Face4Copy[1][0]#
            Face6[2][2] = Face4Copy[2][0]#

            Face2[0][2] = Face6Copy[2][2]#
            Face2[1][2] = Face6Copy[2][1]#
            Face2[2][2] = Face6Copy[2][0]#

            Face4[0][0] = Face5Copy[0][2]#
            Face4[1][0] = Face5Copy[0][1]#
            Face4[2][0] = Face5Copy[0][0]#

            #clockwise face 3 
            Face3[0][0] = Face3Copy[2][0]
            Face3[0][1] = Face3Copy[1][0]
            Face3[0][2] = Face3Copy[0][0]
            Face3[1][2] = Face3Copy[0][1]
            Face3[2][2] = Face3Copy[0][2]
            Face3[2][1] = Face3Copy[1][2]
            Face3[2][0] = Face3Copy[2][2]
            Face3[1][0] = Face3Copy[2][1]

        elif Movement == "Bi": #back face to right ("Bi")
            self.Moves.append(MoveNames[5])

            Face5[0][0] = Face4Copy[2][0]#
            Face5[0][1] = Face4Copy[1][0]#
            Face5[0][2] = Face4Copy[0][0]#

            Face6[2][0] = Face2Copy[2][2]#
            Face6[2][1] = Face2Copy[1][2]#
            Face6[2][2] = Face2Copy[0][2]#

            Face2[0][2] = Face5Copy[0][0]#
            Face2[1][2] = Face5Copy[0][1]#
            Face2[2][2] = Face5Copy[0][2]#

            Face4[0][0] = Face6Copy[2][0]#
            Face4[1][0] = Face6Copy[2][1]#
            Face4[2][0] = Face6Copy[2][2]#

            #anti clock face 3 
            Face3[0][0] = Face3Copy[0][2]
            Face3[0][1] = Face3Copy[1][2]
            Face3[0][2] = Face3Copy[2][2]
            Face3[1][2] = Face3Copy[2][1]
            Face3[2][2] = Face3Copy[2][0]
            Face3[2][1] = Face3Copy[1][0]
            Face3[2][0] = Face3Copy[0][0]
            Face3[1][0] = Face3Copy[0][1]

        elif Movement == "D": #bottom right ("D")
            self.Moves.append(MoveNames[6])
            for i in range(GRID_SIZE):
                Face1[2][i] = Face4Copy[2][i]#
                Face2[2][i] = Face1Copy[2][i]#
                Face3[2][i] = Face2Copy[2][i]#
                Face4[2][i] = Face3Copy[2][i]#

            #face 6 clockwise 
            Face6[0][0] = Face6Copy[2][0]
            Face6[0][1] = Face6Copy[1][0]
            Face6[0][2] = Face6Copy[0][0]
            Face6[1][2] = Face6Copy[0][1]
            Face6[2][2] = Face6Copy[0][2]
            Face6[2][1] = Face6Copy[1][2]
            Face6[2][0] = Face6Copy[2][2]
            Face6[1][0] = Face6Copy[2][1]

        elif Movement == "Di": #bottom left  ("Di")
            self.Moves.append(MoveNames[7])
            for i in range(GRID_SIZE):
                Face1[2][i] = Face2Copy[2][i]#
                Face2[2][i] = Face3Copy[2][i]#
                Face3[2][i] = Face4Copy[2][i]#
                Face4[2][i] = Face1Copy[2][i]#

            #face 6 anti clock 
            Face6[0][0] = Face6Copy[0][2]
            Face6[0][1] = Face6Copy[1][2]
            Face6[0][2] = Face6Copy[2][2]
            Face6[1][2] = Face6Copy[2][1]
            Face6[2][2] = Face6Copy[2][0]
            Face6[2][1] = Face6Copy[1][0]
            Face6[2][0] = Face6Copy[0][0]
            Face6[1][0] = Face6Copy[0][1]

        elif Movement == "F": #front right ("F")
            self.Moves.append(MoveNames[8])

            Face5[2][0] = Face4Copy[2][2]#
            Face5[2][1] = Face4Copy[1][2]#
            Face5[2][2] = Face4Copy[0][2]#

            Face2[0][0] = Face5Copy[2][0]#
            Face2[1][0] = Face5Copy[2][1]#
            Face2[2][0] = Face5Copy[2][2]#

            Face4[0][2] = Face6Copy[0][0]#
            Face4[1][2] = Face6Copy[0][1]#
            Face4[2][2] = Face6Copy[0][2]#

            Face6[0][0] = Face2Copy[2][0]#
            Face6[0][1] = Face2Copy[1][0]#
            Face6[0][2] = Face2Copy[0][0]#

            #face 1 clockwise 
            Face1[0][0] = Face1Copy[2][0]
            Face1[0][1] = Face1Copy[1][0]
            Face1[0][2] = Face1Copy[0][0]
            Face1[1][2] = Face1Copy[0][1]
            Face1[2][2] = Face1Copy[0][2]
            Face1[2][1] = Face1Copy[1][2]
            Face1[2][0] = Face1Copy[2][2]
            Face1[1][0] = Face1Copy[2][1]

        elif Movement == "Fi": #front left ("Fi")
            self.Moves.append(MoveNames[9])

            Face5[2][0] = Face2Copy[0][0]#
            Face5[2][1] = Face2Copy[1][0]#
            Face5[2][2] = Face2Copy[2][0]#

            Face2[0][0] = Face6Copy[0][2]#
            Face2[1][0] = Face6Copy[0][1]#
            Face2[2][0] = Face6Copy[0][0]#

            Face4[0][2] = Face5Copy[2][2]#
            Face4[1][2] = Face5Copy[2][1]#
            Face4[2][2] = Face5Copy[2][0]#

            Face6[0][0] = Face4Copy[0][2]#
            Face6[0][1] = Face4Copy[1][2]#
            Face6[0][2] = Face4Copy[2][2]#

            #face 1 anti 
            Face1[0][0] = Face1Copy[0][2]
            Face1[0][1] = Face1Copy[1][2]
            Face1[0][2] = Face1Copy[2][2]
            Face1[1][2] = Face1Copy[2][1]
            Face1[2][2] = Face1Copy[2][0]
            Face1[2][1] = Face1Copy[1][0]
            Face1[2][0] = Face1Copy[0][0]
            Face1[1][0] = Face1Copy[0][1]

        elif Movement == "U": #top left ("U")
            self.Moves.append(MoveNames[10])
            for i in range(GRID_SIZE):
                Face1[0][i] = Face2Copy[0][i]#
                Face2[0][i] = Face3Copy[0][i]#
                Face3[0][i] = Face4Copy[0][i]#
                Face4[0][i] = Face1Copy[0][i]#

            #face 5 clockwise 
            Face5[0][0] = Face5Copy[2][0]
            Face5[0][1] = Face5Copy[1][0]
            Face5[0][2] = Face5Copy[0][0]
            Face5[1][2] = Face5Copy[0][1]
            Face5[2][2] = Face5Copy[0][2]
            Face5[2][1] = Face5Copy[1][2]
            Face5[2][0] = Face5Copy[2][2]
            Face5[1][0] = Face5Copy[2][1]

        elif Movement == "Ui": #top right ("Ui")
            self.Moves.append(MoveNames[11])
            for i in range(GRID_SIZE):
                Face1[0][i] = Face4Copy[0][i]#
                Face2[0][i] = Face1Copy[0][i]#
                Face3[0][i] = Face2Copy[0][i]#
                Face4[0][i] = Face3Copy[0][i]#
        
            #face 5 anti
            Face5[0][0] = Face5Copy[0][2]
            Face5[0][1] = Face5Copy[1][2]
            Face5[0][2] = Face5Copy[2][2]
            Face5[1][2] = Face5Copy[2][1]
            Face5[2][2] = Face5Copy[2][0]
            Face5[2][1] = Face5Copy[1][0]
            Face5[2][0] = Face5Copy[0][0]
            Face5[1][0] = Face5Copy[0][1]

        elif Movement == "M": #middle to left ("M")
            self.Moves.append(MoveNames[12])
            for i in range(GRID_SIZE):
                Face1[1][i] = Face2Copy[1][i]#
                Face2[1][i] = Face3Copy[1][i]#
                Face3[1][i] = Face4Copy[1][i]#
                Face4[1][i] = Face1Copy[1][i]#


def SolveDaisy(Cube):

    YellowFace = Cube.Face5 #face with yellow center

    if YellowFace[0][1] == "W" and YellowFace[2][1] == "W" and YellowFace[1][0] == "W" and YellowFace[1][2] == "W":
        return #add check all of future steps 

     
    LoopNum = 0
    while True: 
        LoopNum +=1
        for TryUp in range(4): #up
            if YellowFace[0][1] == "W":
                break
            elif Cube.Face3[0][1] == "W": # if face inverted 
                #Bi, U, Ri, Ui
                Cube.Move("Bi")
                Cube.Move("U")
                Cube.Move("Ri")
                Cube.Move("Ui")
                break
            else:
                Cube.Move("Bi")#move back face right 


        for TryDown in range(4): #down
            if YellowFace[2][1] == "W":
                break
            elif Cube.Face1[0][1] == "W":
                #Fi, U, Li, Ui
                Cube.Move("Fi")
                Cube.Move("U")
                Cube.Move("Li")
                Cube.Move("Ui")
                break
            else:
                Cube.Move("F") #move front face right 

        for TryLeft in range(4): #left
            if YellowFace[1][0] == "W":
                break
            elif Cube.Face4[0][1] == "W":
                #Li, U, Bi, Ui
                Cube.Move("Li")
                Cube.Move("U")
                Cube.Move("Bi")
                Cube.Move("Ui")
                break
            else:
                Cube.Move("Li") #move left face up 

        for TryRight in range(4): #right
            if YellowFace[1][2] == "W":
                break
            elif Cube.Face2[0][1] == "W":
                #Ri, U, Fi, Ui
                Cube.Move("Ri")
                Cube.Move("U")
                Cube.Move("Fi")
                Cube.Move("Ui")
                break
            else:
                Cube.Move("R") #move right face up 

        if YellowFace[0][1] == "W" and YellowFace[2][1] == "W" and YellowFace[1][0] == "W" and YellowFace[1][2] == "W":
            break

        Cube.Move("M")# rotate down face to shufle and hofully get the white in rotation 
        Cube.Move("D")

        if LoopNum >5:
            print("Loop Broke")
            break

    while Cube.Face1[1][1] != "B":
        Cube.Move("M")
        
def SolveWhiteCross(Cube):

    WhiteFace = Cube.Face6

    if WhiteFace[0][1] == "W" and WhiteFace[1][0] == "W" and WhiteFace[1][2] == "W" and WhiteFace[2][1] == "W":
        if Cube.Face1[2][1] == "B" and Cube.Face2[2][1] == "R" and Cube.Face3[2][1] == "G" and Cube.Face1[2][1] == "O":
            return # if already solved return 

    YellowFace = Cube.Face5 #face with yellow center 

    for SetBlue in range(4): #align blue face with white edge 
        if Cube.Face1[0][1] == "B" and YellowFace[2][1] == "W":
            Cube.Move("F")
            Cube.Move("F")
            break
        else:
            Cube.Move("U")#TOP FACE LEFT 

    for SetRed in range(4): #align red face with white edge 
        if Cube.Face2[0][1] == "R" and YellowFace[1][2] == "W":
            Cube.Move("R")
            Cube.Move("R")
            break
        else:
            Cube.Move("U")#TOP FACE LEFT 

    for SetGreen in range(4): #align green face with white edge 
        if Cube.Face3[0][1] == "G" and YellowFace[0][1] == "W":
            Cube.Move("B")
            Cube.Move("B")
            break
        else:
            Cube.Move("U")#TOP FACE LEFT 

    for SetOrange in range(4): #align orange face with white edge 
        if Cube.Face4[0][1] == "O" and YellowFace[1][0] == "W":
            Cube.Move("L")
            Cube.Move("L")
            break
        else:
            Cube.Move("U")#TOP FACE LEFT 
    
def SolveWhiteCorners(Cube):
    
    YellowFace = Cube.Face5
    WhiteFace = Cube.Face6

    for FrontFace in range(2):
        CurrentFace = eval(f"Cube.Face{5+FrontFace}")



    for SideFace in range(4):

        CurrentFace = eval(f"Cube.Face{SideFace+1}")
        TL = CurrentFace[0][0] # top left
        TR = CurrentFace[0][2] #top right 
        BL = CurrentFace[2][0] #bottom left 
        BR = CurrentFace[2][2] #Bottom right 
        
        #if TL == "W"

        

  
def ShowMoves(Cube):

    CurrentMoveNum = 1

    while True:

        CurrentMove = Cube.Moves[CurrentMoveNum-1]
        MoveImage = cv2.imread(f"Moves\\{CurrentMove}.png")
        MoveImage = cv2.resize(MoveImage, (0,0), fx=3,fy=3)

        cv2.putText(MoveImage,f"{CurrentMoveNum}", (10,20), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0,0,0), 1)
        cv2.imshow("Move:", MoveImage)
        
        k = cv2.waitKeyEx(1)
        if k == 2424832 and CurrentMoveNum > 1: #left
            CurrentMoveNum -= 1
        if k == 2555904 and CurrentMoveNum <= len(Cube.Moves)-1: #right
            CurrentMoveNum += 1
        if k == 27: #esc key to exit
            break
    


def SolveCube():

    Cube = CubeOBJ()


    SolveDaisy(Cube)
    #Cube.PrintFaces()
    
    SolveWhiteCross(Cube)

    Cube.Move("U", 6)

    Cube.PrintFaces()
    
    

    print(Cube.Moves)
    ShowMoves(Cube)






#SolveCube()





#-----------------solver copy 2 


YellowFace = Cube.Face5 #face with yellow center
    

    LoopNum = 0
    while True: 
        LoopNum +=1
        
        for Edge in range(4):
            CurrentFace = Edge+1
            
            for RotateFace in range(4):

                Edge1 = YellowFace[2][1]
                Edge2 = YellowFace[1][2]
                Edge3 = YellowFace[0][1]
                Edge4 = YellowFace[1][0]

                CurrentEdge = eval(f"Edge{CurrentFace}")
                CurrentInvertedEdge = eval(f"Cube.Face{CurrentFace}[0][1]")

                #print(f"cur edge {CurrentEdge}")
                #print(eval(f"Cube.Face{CurrentFace}"))

                if CurrentEdge == "W":
                    break
                elif CurrentInvertedEdge == "W":
                    print(f"inverting edge of face : {CurrentFace} since its curent inverted edge color is {CurrentInvertedEdge}")
                    Cube.Move("Fi", CurrentFace)
                    Edge2 = YellowFace[1][2]
                    print(Edge2)
                    Cube.Move("U", CurrentFace)
                    Edge2 = YellowFace[1][2]
                    print(Edge2)
                    Cube.Move("Li", CurrentFace)
                    Edge2 = YellowFace[1][2]
                    print(Edge2)
                    Cube.Move("Ui", CurrentFace)
                    Edge2 = YellowFace[1][2]
                    print(Edge2)
                    print("new inverted face is: "+eval(f"Edge{CurrentFace}"))
                    break
                else:
                    
                    print(f"rotating face: {CurrentFace} since top face is:")
                    print(eval(f"Edge{CurrentFace}"))
                    Cube.Move("F", CurrentFace) #move front face right 

                
                
            

        if YellowFace[0][1] == "W" and YellowFace[2][1] == "W" and YellowFace[1][0] == "W" and YellowFace[1][2] == "W":
            break

        print("shuffle ")
        #Cube.Move("M")# rotate down face to shufle and hofully get the white in rotation 
        Cube.Move("D")

        if LoopNum >5:
            print("Loop Broke")
            break

    while Cube.Face1[1][1] != "B":
        Cube.Move("M")







################33


for Face in range(1,5): #1-4

        CurrentFace = eval(f"Cube.Face{Face}")

        CurrentEdge = None
        if Face == 1:
            CurrentEdge = Cube.Face5[2][1]
        elif Face == 2:
            CurrentEdge = Cube.Face5[1][2]
        elif Face == 3:
            CurrentEdge = Cube.Face5[0][1]
        elif Face == 4:
            CurrentEdge = Cube.Face5[1][0]

        if CurrentEdge == "W":
            print(f"Face {Face} is solved")
            continue


        while True:

            Edge1 = CurrentFace[0][1] 
            Edge2 = CurrentFace[1][0] 
            Edge3 = CurrentFace[1][2]  
            Edge4 = CurrentFace[2][1]

            if Edge1 == "W" or Edge2 == "W" or Edge3 == "W" or Edge4 == "W":

                if Edge1 == "W":
                    print(f"solving face {Face}")

                    print(f"edge 1: {Cube.Face2[0][1]}")

                    print("before")
                    for i in Cube.Face5:
                        print(i)

                    Cube.Move("Fi", Face)  
                    Cube.Move("U", Face)
                    Cube.Move("Li", Face)
                    Cube.Move("Ui", Face)

                    

                    print("after")
                    for i in Cube.Face5:
                        print(i)


                    break
                else:
                    Cube.Move("F", Face)
                    
            else:
                #print("rotation")
                Cube.Move("R", Face)
                Cube.Move("D", Face)
                Cube.Move("Ri", Face)
        
        print(f"Face {Face} was solved ")