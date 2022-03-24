import copy
import cv2
import time
import numpy as np 
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

            Face1Copy = copy.deepcopy(self.Face2) 
            Face2Copy = copy.deepcopy(self.Face3)
            Face3Copy = copy.deepcopy(self.Face4)
            Face4Copy = copy.deepcopy(self.Face1)

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

            Face1Copy = copy.deepcopy(self.Face3) 
            Face2Copy = copy.deepcopy(self.Face4)
            Face3Copy = copy.deepcopy(self.Face1)
            Face4Copy = copy.deepcopy(self.Face2)

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

            Face1Copy = copy.deepcopy(self.Face4) 
            Face2Copy = copy.deepcopy(self.Face1)
            Face3Copy = copy.deepcopy(self.Face2)
            Face4Copy = copy.deepcopy(self.Face3)

            MoveNames[0] = "F"
            MoveNames[1] = "Fi"
            MoveNames[2] = "B"
            MoveNames[3] = "Bi"
            MoveNames[4] = "R"
            MoveNames[5] = "Ri"
            MoveNames[8] = "L"
            MoveNames[9] = "Li"

        elif FrontFaceNum == 5: # UNFINISHED!!! 
            Face1 = self.Face5
            Face3 = self.Face6
            Face5 = self.Face3
            Face6 = self.Face1

            Face1Copy = copy.deepcopy(self.Face5) 
            Face3Copy = copy.deepcopy(self.Face6)
            Face5Copy = copy.deepcopy(self.Face3)
            Face6Copy = copy.deepcopy(self.Face1)

            MoveNames[4] = "D"
            MoveNames[5] = "Di"
            MoveNames[6] = "F"
            MoveNames[7] = "Fi"
            MoveNames[8] = "U"
            MoveNames[9] = "Ui"
            MoveNames[10] = "B"
            MoveNames[11] = "Bi"

        elif FrontFaceNum == 6: # UNFINISHED!!!  
            Face1 = self.Face6
            Face3 = self.Face5
            Face5 = self.Face1
            Face6 = self.Face3

            Face1Copy = copy.deepcopy(self.Face6) 
            Face3Copy = copy.deepcopy(self.Face5)
            Face5Copy = copy.deepcopy(self.Face1)
            Face6Copy = copy.deepcopy(self.Face3)

            MoveNames[4] = "U"
            MoveNames[5] = "Ui"
            MoveNames[6] = "B"
            MoveNames[7] = "Bi"
            MoveNames[8] = "D"
            MoveNames[9] = "Di"
            MoveNames[10] = "F"
            MoveNames[11] = "Fi"



        if Movement == "R": #right up* ("R") FINISHED
            self.Moves.append(MoveNames[0])
            
            if FrontFaceNum == 1:
                self.Move("F",2)
            elif FrontFaceNum == 2:
                self.Move("F",3)
            elif FrontFaceNum == 3:
                self.Move("F",4)
            elif FrontFaceNum == 4:
                self.Move("F",1)
  
        elif Movement == "Ri": #right down* ("Ri") FINISHED
            self.Moves.append(MoveNames[1])
            
            if FrontFaceNum == 1:
                self.Move("Fi",2)
            elif FrontFaceNum == 2:
                self.Move("Fi",3)
            elif FrontFaceNum == 3:
                self.Move("Fi",4)
            elif FrontFaceNum == 4:
                self.Move("Fi",1)

        elif Movement == "L": #left down* ("L") FINISHED
            self.Moves.append(MoveNames[2])
            
            if FrontFaceNum == 1:
                self.Move("F",4)
            elif FrontFaceNum == 2:
                self.Move("F",1)
            elif FrontFaceNum == 3:
                self.Move("F",2)
            elif FrontFaceNum == 4:
                self.Move("F",3)

        elif Movement == "Li": #left up* ("Li") FINISHED
            self.Moves.append(MoveNames[3])
            
            if FrontFaceNum == 1:
                self.Move("Fi",4)
            elif FrontFaceNum == 2:
                self.Move("Fi",1)
            elif FrontFaceNum == 3:
                self.Move("Fi",2)
            elif FrontFaceNum == 4:
                self.Move("Fi",3)

        elif Movement == "B": #back face to left  ("B") FINISHED
            self.Moves.append(MoveNames[4])
  
            if FrontFaceNum == 1:
                self.Move("F",3)
            elif FrontFaceNum == 2:
                self.Move("F",4)
            elif FrontFaceNum == 3:
                self.Move("F",1)
            elif FrontFaceNum == 4:
                self.Move("F",2)

        elif Movement == "Bi": #back face to right ("Bi") FINISHED
            self.Moves.append(MoveNames[5])

            if FrontFaceNum == 1:
                self.Move("Fi",3)
            elif FrontFaceNum == 2:
                self.Move("Fi",4)
            elif FrontFaceNum == 3:
                self.Move("Fi",1)
            elif FrontFaceNum == 4:
                self.Move("Fi",2)

        elif Movement == "D": #bottom right ("D") FINISHED
            self.Moves.append(MoveNames[6])
            for i in range(GRID_SIZE):
                Face1[2][i] = Face4Copy[2][i]#
                Face2[2][i] = Face1Copy[2][i]#
                Face3[2][i] = Face2Copy[2][i]#
                Face4[2][i] = Face3Copy[2][i]#

            #face 6 clockwise 
            Face6[:] = [[*col][::-1] for col in zip(*Face6)] #clockwise 

        elif Movement == "Di": #bottom left  ("Di") FINISHED
            self.Moves.append(MoveNames[7])
            for i in range(GRID_SIZE):
                Face1[2][i] = Face2Copy[2][i]#
                Face2[2][i] = Face3Copy[2][i]#
                Face3[2][i] = Face4Copy[2][i]#
                Face4[2][i] = Face1Copy[2][i]#

            #face 6 anti clock 
            Face6[:] = [[*col] for col in zip(*Face6)][::-1] #anticlock

        elif Movement == "F": #front right ("F") FINISHED
            self.Moves.append(MoveNames[8])

            #Rotate top and bot faces to resue the code
            if FrontFaceNum == 2:
                for _ in range(1):
                    Face5[:] = [[*col][::-1] for col in zip(*Face5)] #clockwise 
                    Face6[:] = [[*col] for col in zip(*Face6)][::-1] #anticlock
            elif FrontFaceNum == 3:
                for _ in range(2):
                    Face5[:] = [[*col][::-1] for col in zip(*Face5)] #clockwise 
                    Face6[:] = [[*col] for col in zip(*Face6)][::-1] #anticlock
            elif FrontFaceNum == 4:
                for _ in range(1):
                    Face6[:] = [[*col][::-1] for col in zip(*Face6)] #clockwise 
                    Face5[:] = [[*col] for col in zip(*Face5)][::-1] #anticlock

            for i in range(GRID_SIZE):
                Face2[i][0] = Face5[2][i]#in this case its not grabbing from the copy since that one was not rotated 
                Face4[i][2] = Face6[0][i]#

            Face5[2][0] = Face4Copy[2][2]#-
            Face5[2][1] = Face4Copy[1][2]#-
            Face5[2][2] = Face4Copy[0][2]#-

            Face6[0][0] = Face2Copy[2][0]#
            Face6[0][1] = Face2Copy[1][0]#
            Face6[0][2] = Face2Copy[0][0]#

            #face 1 clockwise 
            Face1[:] = [[*col][::-1] for col in zip(*Face1Copy)]

            #return faces to normal
            if FrontFaceNum == 2:
                for _ in range(1):
                    Face6[:] = [[*col][::-1] for col in zip(*Face6)] #clockwise 
                    Face5[:] = [[*col] for col in zip(*Face5)][::-1] #anticlock
            elif FrontFaceNum == 3:
                for _ in range(2):
                    Face6[:] = [[*col][::-1] for col in zip(*Face6)] #clockwise 
                    Face5[:] = [[*col] for col in zip(*Face5)][::-1] #anticlock
            elif FrontFaceNum == 4:
                for _ in range(1):
                    Face5[:] = [[*col][::-1] for col in zip(*Face5)] #clockwise 
                    Face6[:] = [[*col] for col in zip(*Face6)][::-1] #anticlock

        elif Movement == "Fi": #front left ("Fi") FINISHED
            self.Moves.append(MoveNames[9])

            #Rotate top and bot faces to resue the code
            if FrontFaceNum == 2:
                for _ in range(1):
                    Face5[:] = [[*col][::-1] for col in zip(*Face5)] #clockwise 
                    Face6[:] = [[*col] for col in zip(*Face6)][::-1] #anticlock
            elif FrontFaceNum == 3:
                for _ in range(2):
                    Face5[:] = [[*col][::-1] for col in zip(*Face5)] #clockwise 
                    Face6[:] = [[*col] for col in zip(*Face6)][::-1] #anticlock
            elif FrontFaceNum == 4:
                for _ in range(1):
                    Face6[:] = [[*col][::-1] for col in zip(*Face6)] #clockwise 
                    Face5[:] = [[*col] for col in zip(*Face5)][::-1] #anticlock


            Face2[0][0] = Face6[0][2]#verified
            Face2[1][0] = Face6[0][1]#verified
            Face2[2][0] = Face6[0][0]#verified

            Face4[0][2] = Face5[2][2]#verified
            Face4[1][2] = Face5[2][1]#verified
            Face4[2][2] = Face5[2][0]#verified

            for i in range(GRID_SIZE):
                Face5[2][i] = Face2Copy[i][0]#
                Face6[0][i] = Face4Copy[i][2]#

            #face 1 anti 
            Face1[:] = [[*col] for col in zip(*Face1Copy)][::-1]
            
            #return faces to normal
            if FrontFaceNum == 2:
                for _ in range(1):
                    Face6[:] = [[*col][::-1] for col in zip(*Face6)] #clockwise 
                    Face5[:] = [[*col] for col in zip(*Face5)][::-1] #anticlock
            elif FrontFaceNum == 3:
                for _ in range(2):
                    Face6[:] = [[*col][::-1] for col in zip(*Face6)] #clockwise 
                    Face5[:] = [[*col] for col in zip(*Face5)][::-1] #anticlock
            elif FrontFaceNum == 4:
                for _ in range(1):
                    Face5[:] = [[*col][::-1] for col in zip(*Face5)] #clockwise 
                    Face6[:] = [[*col] for col in zip(*Face6)][::-1] #anticlock

        elif Movement == "U": #top left ("U") FINISHED
            self.Moves.append(MoveNames[10])
            for i in range(GRID_SIZE):
                Face1[0][i] = Face2Copy[0][i]#
                Face2[0][i] = Face3Copy[0][i]#
                Face3[0][i] = Face4Copy[0][i]#
                Face4[0][i] = Face1Copy[0][i]#

            #face 5 clockwise 
            Face5[:] = [[*col][::-1] for col in zip(*Face5)] #clockwise 

        elif Movement == "Ui": #top right ("Ui") FINISHED
            self.Moves.append(MoveNames[11])
            for i in range(GRID_SIZE):
                Face1[0][i] = Face4Copy[0][i]#
                Face2[0][i] = Face1Copy[0][i]#
                Face3[0][i] = Face2Copy[0][i]#
                Face4[0][i] = Face3Copy[0][i]#
        
            #face 5 anti
            Face5[:] = [[*col] for col in zip(*Face5)][::-1] #anticlock

        elif Movement == "M": #middle to left ("M")
            self.Moves.append(MoveNames[12])
            for i in range(GRID_SIZE):
                Face1[1][i] = Face2Copy[1][i]#
                Face2[1][i] = Face3Copy[1][i]#
                Face3[1][i] = Face4Copy[1][i]#
                Face4[1][i] = Face1Copy[1][i]#

        

def SolveDaisy(Cube):
    if Cube.Face5[2][1] == "W" and Cube.Face5[1][2] == "W" and Cube.Face5[0][1] == "W" and Cube.Face5[1][0] == "W":
        print("Daisy already solved")
        return #if already solved exit
    elif Cube.Face6[2][1] == "W" and Cube.Face6[1][2] == "W" and Cube.Face6[0][1] == "W" and Cube.Face6[1][0] == "W":
        print("no need for Daisy, white cross already solved")
        return #if already solved exit

    for Edge in range(1,5): #1-4
        
        i = 0
        while True:
            i += 1

            TopEdge1 = Cube.Face5[2][1] 
            TopEdge2 = Cube.Face5[1][2] 
            TopEdge3 = Cube.Face5[0][1]  
            TopEdge4 = Cube.Face5[1][0] 

            if eval(f"TopEdge{Edge}") == "W":
                #print(f"Edge {Edge} already solved")
                break
            elif eval(f"Cube.Face{Edge}[0][1]") == "W": #if inverted
                #print(f"solving {Edge} since its inverted")
                Cube.Move("Fi", Edge)  
                Cube.Move("U", Edge)
                Cube.Move("Li", Edge)
                Cube.Move("Ui", Edge)
                break
            else:
                #print("rotating")
                Cube.Move("F", Edge)
                if i%3 == 0:
                    #print("shufuling")
                    if i <= 9:
                        Cube.Move("D", Edge)
                    else:
                        Cube.Move("M")

        #print(f"solved edge {Edge}")
    
    while Cube.Face1[1][1] != "B":
        Cube.Move("M")

    print("Solved Daisy")

def SolveWhiteCross(Cube):

    for SetFace in range(1,5):

        while True:
            Face1, Face2, Face3, Face4 = "B","R","G","O"
            Edge1, Edge2, Edge3, Edge4 = Cube.Face5[2][1], Cube.Face5[1][2], Cube.Face5[0][1], Cube.Face5[1][0]

            if eval(f"Cube.Face{SetFace}[0][1]") == eval(f"Face{SetFace}") and eval(f"Edge{SetFace}") == "W":
                Cube.Move("F", SetFace)
                Cube.Move("F", SetFace)
                break
            else:
                Cube.Move("U", SetFace)#TOP FACE LEFT
        
        if False : #debug
            print(f"solved face {SetFace}")
            
            print("face 5")
            for i in Cube.Face5:
                print(i)
            
            print("face 6")
            for i in Cube.Face6:
                print(i)
        
    print("Solved White Cross")

def SolveWhiteCorners(Cube):

    TopCurrentCorner = ["N","N","N"] #Front side, left side, top side 
    BottomCurrentCorner = ["N","N","N"] #Front side, left side, bottom side

    for Face in range(1,5): #first check for any white corners in white face (bottom face )

        if Face == 1:
            BottomCurrentCorner = [Cube.Face1[2][0], Cube.Face4[2][2], Cube.Face6[0][0]]
        elif Face == 2:
            BottomCurrentCorner = [Cube.Face2[2][0], Cube.Face1[2][2], Cube.Face6[0][2]]
        elif Face == 3:
            BottomCurrentCorner = [Cube.Face3[2][0], Cube.Face2[2][2], Cube.Face6[2][2]]
        elif Face == 4:
            BottomCurrentCorner = [Cube.Face3[2][0], Cube.Face2[2][2], Cube.Face6[2][0]]

        if "W" in BottomCurrentCorner: #if any of the sides are white 

            LeftFace = eval(f"Cube.Face{Face-1}") if Face != 1 else Cube.Face4
            FrontFace = eval(f"Cube.Face{Face}")
            
            #check if its in correct order else move to top 
            if BottomCurrentCorner[2] == "W" and FrontFace[2][0] == BottomCurrentCorner[0] and LeftFace[2][2] == BottomCurrentCorner[1]:
                continue
            else: #MOVE FACE TO TOP LAYER 
                Cube.Move("Li",Face)
                Cube.Move("Ui",Face)
                Cube.Move("L", Face)


            '''
            if BottomCurrentCorner[2] == "W" and eval(f"Cube.Face{ColorNums[BottomCurrentCorner[0]]}[2][0]") == BottomCurrentCorner[0]:
                continue


            #check if its in correct order else move to top 
            if eval(f"BottomFaceEdge{Face}") == "W" and FrontFace[2][0] == FrontFace[1][1] and LeftFace[2][2] == LeftFace[1][1]:
                continue
            '''

    for Face in range(1,5): #check and move corners in yellow face to white face in correct pos 
        
        while True: #loop until a valid edge with with appears 

            if Face == 1:
                TopCurrentCorner = [Cube.Face1[0][0], Cube.Face4[0][2], Cube.Face5[2][0]]
            elif Face == 2:
                TopCurrentCorner = [Cube.Face2[0][0], Cube.Face1[0][2], Cube.Face5[2][2]]
            elif Face == 3:
                TopCurrentCorner = [Cube.Face3[0][0], Cube.Face2[0][2], Cube.Face5[0][2]]
            elif Face == 4:
                TopCurrentCorner = [Cube.Face4[0][0], Cube.Face3[0][2], Cube.Face5[0][0]]

            if "W" in TopCurrentCorner:
                #rotate top face until the 2 non withe colors align with the center of faces 
                
                for Rotation in range(1,4): # 1-3

                    LeftFace = eval(f"Cube.Face{Face-1}") if Face != 1 else Cube.Face4
                    FrontFace = eval(f"Cube.Face{Face}")
                    TopFaceEdge1 = Cube.Face5[2][0]
                    TopFaceEdge2 = Cube.Face5[2][2]
                    TopFaceEdge3 = Cube.Face5[0][2]
                    TopFaceEdge4 = Cube.Face5[0][0]

                    #--------------make sure all posibilites exist 
                    if (
                        (LeftFace[0][2] == FrontFace[1][1] or FrontFace[0][0] == FrontFace[1][1] or eval(f"TopFaceEdge{Face}") == FrontFace[1][1]) and 
                        (LeftFace[0][2] == LeftFace[1][1] or FrontFace[0][0] == LeftFace[1][1] or eval(f"TopFaceEdge{Face}") == LeftFace[1][1])
                    ):
                        #move edge into bottom face (since we veriefed its correct)

                        #check what movement to do depending on where the white side is in the corner
                        
                        if eval(f"TopFaceEdge{Face}") == "W": #if top face is white rotate it so that the white side is now the front
                            Cube.Move("F",Face)
                            Cube.Move("Ui",Face)
                            Cube.Move("Fi",Face)
                            Cube.Move("U",Face)
                            Cube.Move("U",Face)
                            #NOW THAT WHITE FACE IS IN FRONT MOVE IT TO THE WHITE FACE (FACE6)
                            Cube.Move("Ui",Face)
                            Cube.Move("Li",Face)
                            Cube.Move("U",Face)
                            Cube.Move("L",Face)
                            

                        if FrontFace[0][0] == "W": #if frotn face is white
                            Cube.Move("Ui",Face)
                            Cube.Move("Li",Face)
                            Cube.Move("U",Face)
                            Cube.Move("L",Face)

                            
                        elif LeftFace[0][2] == "W": #if left face is white
                            Cube.Move("U",Face)
                            Cube.Move("F",Face)
                            Cube.Move("Ui",Face)
                            Cube.Move("Fi",Face)
                        

                    else:
                        Cube.Move("U",Face)

                    #alaign so that both colors 
                    
                break #stop loop since we found and solved white edge 
                
            else:
                Cube.Move("U", Face) #move top face to cicle and find a edge with white 

def SolveMiddleEdges(Cube):
    pass






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
    #Cube.PrintFaces()

    SolveWhiteCorners(Cube)
    #Cube.PrintFaces()

    SolveMiddleEdges(Cube)
    Cube.PrintFaces()


    print(Cube.Moves)
    ShowMoves(Cube)
    

    






#SolveCube()