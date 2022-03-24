from App import FaceNum
import copy
import cv2
import time
import numpy as np 

GRID_SIZE = 3

Face1 = [
    ["B","B","B"],
    ["B","B","B"],
    ["B","B","B"]
]

Face2 = [
    ["R","R","R"],
    ["R","R","R"],
    ["R","R","R"]
]

Face3 = [
    ["G","G","G"],
    ["G","G","G"],
    ["G","G","G"]
]

Face4 = [
    ["O","O","O"],
    ["O","O","O"],
    ["O","O","O"]
]

Face5 = [
    ["Y","Y","*"],
    ["Y","Y","*"],
    ["Y","Y","*"]
]

Face6 = [
    ["W","W","W"],
    ["W","W","W"],
    ["W","W","W"]
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

        Face1Copy = copy.deepcopy(Face1) 
        Face2Copy = copy.deepcopy(Face2)
        Face3Copy = copy.deepcopy(Face3)
        Face4Copy = copy.deepcopy(Face4)
        Face5Copy = copy.deepcopy(Face5)
        Face6Copy = copy.deepcopy(Face6)

        
        if FrontFaceNum == 2:
            Face1 = self.Face2
            Face2 = self.Face3
            Face3 = self.Face4
            Face4 = self.Face1

            Face1Copy = copy.deepcopy(Face2) 
            Face2Copy = copy.deepcopy(Face3)
            Face3Copy = copy.deepcopy(Face4)
            Face4Copy = copy.deepcopy(Face1)

            #rotate
            #Face1[:] = np.rot90(Face1, 1)
            Face5Copy = np.rot90(Face5Copy, -1)
            Face6Copy = np.rot90(Face6Copy, 1)

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

            Face1Copy = copy.deepcopy(Face3) 
            Face2Copy = copy.deepcopy(Face4)
            Face3Copy = copy.deepcopy(Face1)
            Face4Copy = copy.deepcopy(Face2)

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

            Face1Copy = copy.deepcopy(Face4) 
            Face2Copy = copy.deepcopy(Face1)
            Face3Copy = copy.deepcopy(Face2)
            Face4Copy = copy.deepcopy(Face3)

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
            Face3 = self.Face6
            Face5 = self.Face3
            Face6 = self.Face1

            Face1Copy = copy.deepcopy(Face5) 
            Face3Copy = copy.deepcopy(Face6)
            Face5Copy = copy.deepcopy(Face3)
            Face6Copy = copy.deepcopy(Face1)

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
            Face3 = self.Face5
            Face5 = self.Face1
            Face6 = self.Face3

            Face1Copy = copy.deepcopy(Face6) 
            Face3Copy = copy.deepcopy(Face5)
            Face5Copy = copy.deepcopy(Face1)
            Face6Copy = copy.deepcopy(Face3)

            MoveNames[4] = "U"
            MoveNames[5] = "Ui"
            MoveNames[6] = "B"
            MoveNames[7] = "Bi"
            MoveNames[8] = "D"
            MoveNames[9] = "Di"
            MoveNames[10] = "F"
            MoveNames[11] = "Fi"



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
  
            Face5[0][0] = Face2Copy[0][2]#-
            Face5[0][1] = Face2Copy[1][2]#-
            Face5[0][2] = Face2Copy[2][2]#-

            Face6[2][0] = Face4Copy[0][0]#-
            Face6[2][1] = Face4Copy[1][0]#-
            Face6[2][2] = Face4Copy[2][0]#-

            Face2[0][2] = Face6Copy[2][2]#-
            Face2[1][2] = Face6Copy[2][1]#-
            Face2[2][2] = Face6Copy[2][0]#-

            Face4[0][0] = Face5Copy[0][2]#-
            Face4[1][0] = Face5Copy[0][1]#-
            Face4[2][0] = Face5Copy[0][0]#-

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

            Face5[0][0] = Face4Copy[2][0]#-
            Face5[0][1] = Face4Copy[1][0]#-
            Face5[0][2] = Face4Copy[0][0]#-

            Face6[2][0] = Face2Copy[2][2]#-
            Face6[2][1] = Face2Copy[1][2]#-
            Face6[2][2] = Face2Copy[0][2]#-

            Face2[0][2] = Face5Copy[0][0]#-
            Face2[1][2] = Face5Copy[0][1]#-
            Face2[2][2] = Face5Copy[0][2]#-

            Face4[0][0] = Face6Copy[2][0]#-
            Face4[1][0] = Face6Copy[2][1]#-
            Face4[2][0] = Face6Copy[2][2]#-

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

            if FrontFaceNum == 2:
                

            Face5[2][0] = Face4Copy[2][2]#-
            Face5[2][1] = Face4Copy[1][2]#-
            Face5[2][2] = Face4Copy[0][2]#-

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
            Face1 = np.rot90(Face1Copy, -1)

            if FaceNum == 2:
                Face5[:] = np.rot90(Face5,1)
                



        elif Movement == "Fi": #front left ("Fi")
            self.Moves.append(MoveNames[9])

            if FrontFaceNum == 1:
                Face5[2][0] = Face2Copy[0][0]#-
                Face5[2][1] = Face2Copy[1][0]#-
                Face5[2][2] = Face2Copy[2][0]#-

                Face6[0][0] = Face4Copy[0][2]#-
                Face6[0][1] = Face4Copy[1][2]#-
                Face6[0][2] = Face4Copy[2][2]#-
            elif FrontFaceNum == 2:
                Face5[2][2] = Face2Copy[0][0]#-
                Face5[1][2] = Face2Copy[1][0]#-
                Face5[0][2] = Face2Copy[2][0]#-

                Face6[0][2] = Face4Copy[0][2]#-
                Face6[1][2] = Face4Copy[1][2]#-
                Face6[2][2] = Face4Copy[2][2]#-


            Face2[0][0] = Face6Copy[0][2]#
            Face2[1][0] = Face6Copy[0][1]#
            Face2[2][0] = Face6Copy[0][0]#

            Face4[0][2] = Face5Copy[2][2]#
            Face4[1][2] = Face5Copy[2][1]#
            Face4[2][2] = Face5Copy[2][0]#

            #face 1 anti 
            Face1[:] = np.rot90(Face1, 1)
            
            #specific rotations:
            
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


Cube = CubeOBJ()

Cube.Move("F",2)

Cube.PrintFaces()


    
