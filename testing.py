
import copy
import numpy as np 

FaceExample1 = [
    ["1","2","3"],
    ["8","N","4"],
    ["7","6","5"]
]


FaceExample2 = [
    ["7","8","1"],
    ["6","R","2"],
    ["5","4","3"]
]

MoveNames = [  #NOT A 2D LIST JUST ORDED TO MATCH PAIRS
            "R","Ri", #0,1
            "L","Li", #2,3
            "B","Bi", #4,5
            "D","Di", #6,7
            "F","Fi", #8,9
            "U","Ui", #10,11
            "M", #12
        ]

Edge1 = "W"
Edge2 = ""


clockwise = [[*col][::-1] for col in zip(*FaceExample1)]
anticlockwise = [[*col] for col in zip(*FaceExample1)][::-1]

lisstt = ["W","B","R"]

WhiteIndex = lisstt.index("W")

newlist = [Side for Side in lisstt if Side != "W"]

tests = ["1","2"]

test2 = ["0","1","2"]

Face = 4

LeftFace = "s" if Face != 4 else "b"

print(LeftFace)

if (

    (True) and 
    (True)

):
    print("test")




class CubeOBJ:
    def __init__(self):

        #Faces#
        self.Face1 = 1
        self.Face2 = 2
        self.Face3 = 3
        self.Face4 = 4
        self.Face5 = 5
        self.Face6 = 6

CubeTest = CubeOBJ()



'''
anti
self.Face2[0][0] = Face2Copy[0][2]
self.Face2[0][1] = Face2Copy[1][2]
self.Face2[0][2] = Face2Copy[2][2]
self.Face2[1][2] = Face2Copy[2][1]
self.Face2[2][2] = Face2Copy[2][0]
self.Face2[2][1] = Face2Copy[1][0]
self.Face2[2][0] = Face2Copy[0][0]
self.Face2[1][0] = Face2Copy[0][1]


clockwise 
self.Face4[0][0] = Face4Copy[2][0]
self.Face4[0][1] = Face4Copy[1][0]
self.Face4[0][2] = Face4Copy[0][0]
self.Face4[1][2] = Face4Copy[0][1]
self.Face4[2][2] = Face4Copy[0][2]
self.Face4[2][1] = Face4Copy[1][2]
self.Face4[2][0] = Face4Copy[2][2]
self.Face4[1][0] = Face4Copy[2][1]




MoveNames[0] = ""
MoveNames[1] = ""
MoveNames[2] = ""
MoveNames[3] = ""
MoveNames[4] = ""
MoveNames[5] = ""
MoveNames[6] = ""
MoveNames[7] = ""
MoveNames[8] = ""
MoveNames[9] = ""
MoveNames[10] = ""
MoveNames[11] = ""



MoveNames[0] = ""
MoveNames[1] = ""
MoveNames[2] = ""
MoveNames[3] = ""
MoveNames[4] = ""
MoveNames[5] = ""
MoveNames[8] = ""
MoveNames[9] = ""


More efficient way to move a 3x3 2d list like a Rubik's cube ?

I have been learning python for about a month now, to keep practicing I've been working on a project for the past few days that takes pictures of a Rubik's cube and outputs the moves to solve it, up till now I have the scanner that takes 6 images of the cube from each face and stores them into 6 arrays in this format (Face 1-4 are the side faces and top and bottom faces are 5 and 6): 
Face1 = [
    ["R","G","W"],
    ["O","B","R"],
    ["R","Y","R"]]
Now I have to program each of the 12 movements so that I can use them when creating the solving algorithm, what I'm doing is using a for loop to replace each cell with the new color that it would have when a rotation would happen, something like this (This is the move it simulates): 
if Movement == "D": #bottom right ("D")
    for i in range(3):
        Face1[2][i] = Face4Copy[2][i]
        Face2[2][i] = Face1Copy[2][i]
        Face3[2][i] = Face2Copy[2][i]
        Face4[2][i] = Face3Copy[2][i]
 
    #face 6(Bottom) clockwise 
    Face6[0][0] = Face6Copy[2][0]
    Face6[0][1] = Face6Copy[1][0]
    Face6[0][2] = Face6Copy[0][0]
    Face6[1][2] = Face6Copy[0][1]
    Face6[2][2] = Face6Copy[0][2]
    Face6[2][1] = Face6Copy[1][2]
    Face6[2][0] = Face6Copy[2][2]
    Face6[1][0] = Face6Copy[2][1]
But I feel like this is really inefficient way of doing it since there are moves that cannot be automated with a for loop like the full face anti/clockwise rotations and some of the 12 moves involve mixing the top and bottom face with the side faces and when this happens I have to manually set each new position of every cell in every face involved since for example Face5(left column)[0][i] is not in the same  as Face2(left column)[0][i] it would only apply to the side faces: Face1/2/3/4[0][i]  = Face1/2/3/4[0][i]

Is there another way of doing this in a more efficient/less messy way ?

Thanks!











'''


#wip from old system to make front rotation with different faces


'''
            if FrontFaceNum == 1:
                for i in range(GRID_SIZE):
                    Face2[i][0] = Face5Copy[2][i]#
                    Face4[i][2] = Face6Copy[0][i]#

                Face5[2][0] = Face4Copy[2][2]#-
                Face5[2][1] = Face4Copy[1][2]#-
                Face5[2][2] = Face4Copy[0][2]#-

                Face6[0][0] = Face2Copy[2][0]#
                Face6[0][1] = Face2Copy[1][0]#
                Face6[0][2] = Face2Copy[0][0]#


            elif FrontFaceNum == 2:
                for i in range(GRID_SIZE):
                    #print(Face5[0][2])
                    Face5[i][2] = Face4Copy[i][2]#-
                    Face4[i][2] = Face6Copy[i][2]#


                Face6[0][2] = Face2Copy[2][0]#-
                Face6[1][2] = Face2Copy[1][0]#-
                Face6[2][2] = Face2Copy[0][0]#-

                Face2[0][0] = Face5Copy[2][2]#- this is incorrecvt 
                Face2[1][0] = Face5Copy[1][2]#-
                Face2[2][0] = Face5Copy[0][2]#-
            '''



Face5[:] = [[*col][::-1] for col in zip(*Face5)] #clockwise 
Face6[:] = [[*col] for col in zip(*Face6)][::-1] #anticlock