
if Movement == "R": #right up*  
    self.Moves.append("R")
    for i in range(GRID_SIZE):
        self.Face1[i][2] = Face6Copy[i][2]#
        self.Face5[i][2] = Face1Copy[i][2]#

    self.Face6[0][2] = Face3Copy[2][0]#
    self.Face6[1][2] = Face3Copy[1][0]#
    self.Face6[2][2] = Face3Copy[0][0]#

    self.Face3[0][0] = Face5Copy[2][2]#
    self.Face3[1][0] = Face5Copy[1][2]#
    self.Face3[2][0] = Face5Copy[0][2]#

    ###rotate face clockwise 
    self.Face2[0][0] = Face2Copy[2][0]
    self.Face2[0][1] = Face2Copy[1][0]
    self.Face2[0][2] = Face2Copy[0][0]
    self.Face2[1][2] = Face2Copy[0][1]
    self.Face2[2][2] = Face2Copy[0][2]
    self.Face2[2][1] = Face2Copy[1][2]
    self.Face2[2][0] = Face2Copy[2][2]
    self.Face2[1][0] = Face2Copy[2][1]

elif Movement == "Ri": #right down* 
    self.Moves.append("Ri")
    for i in range(GRID_SIZE):
        self.Face1[i][2] = Face5Copy[i][2]#
        self.Face6[i][2] = Face1Copy[i][2]#

    self.Face5[0][2] = Face3Copy[2][0]#
    self.Face5[1][2] = Face3Copy[1][0]#
    self.Face5[2][2] = Face3Copy[0][0]#

    self.Face3[0][0] = Face6Copy[2][2]#
    self.Face3[1][0] = Face6Copy[1][2]#
    self.Face3[2][0] = Face6Copy[0][2]#

    ###rotate face anti-clockwise 
    self.Face2[0][0] = Face2Copy[0][2]
    self.Face2[0][1] = Face2Copy[1][2]
    self.Face2[0][2] = Face2Copy[2][2]
    self.Face2[1][2] = Face2Copy[2][1]
    self.Face2[2][2] = Face2Copy[2][0]
    self.Face2[2][1] = Face2Copy[1][0]
    self.Face2[2][0] = Face2Copy[0][0]
    self.Face2[1][0] = Face2Copy[0][1]

elif Movement == "L": #left down* 
    self.Moves.append("L")
    for i in range(GRID_SIZE):
        self.Face1[i][0] = Face5Copy[i][0]#
        self.Face6[i][0] = Face1Copy[i][0]#

    self.Face3[0][2] = Face6Copy[2][0]#
    self.Face3[1][2] = Face6Copy[1][0]#
    self.Face3[2][2] = Face6Copy[0][0]#

    self.Face5[0][0] = Face3Copy[2][2]#
    self.Face5[1][0] = Face3Copy[1][2]#
    self.Face5[2][0] = Face3Copy[0][2]#

    ###rotate face clockwise 
    self.Face4[0][0] = Face4Copy[2][0]
    self.Face4[0][1] = Face4Copy[1][0]
    self.Face4[0][2] = Face4Copy[0][0]
    self.Face4[1][2] = Face4Copy[0][1]
    self.Face4[2][2] = Face4Copy[0][2]
    self.Face4[2][1] = Face4Copy[1][2]
    self.Face4[2][0] = Face4Copy[2][2]
    self.Face4[1][0] = Face4Copy[2][1]

elif Movement == "Li": #left up*
    self.Moves.append("Li")
    for i in range(GRID_SIZE):
        self.Face1[i][0] = Face6Copy[i][0]#
        self.Face5[i][0] = Face1Copy[i][0]#

    self.Face6[0][0] = Face3Copy[2][2]#
    self.Face6[1][0] = Face3Copy[1][2]#
    self.Face6[2][0] = Face3Copy[0][2]#

    self.Face3[0][2] = Face5Copy[2][0]#
    self.Face3[1][2] = Face5Copy[1][0]#
    self.Face3[2][2] = Face5Copy[0][0]#

    ###rotate face anti-clockwise 
    self.Face4[0][0] = Face4Copy[0][2]
    self.Face4[0][1] = Face4Copy[1][2]
    self.Face4[0][2] = Face4Copy[2][2]
    self.Face4[1][2] = Face4Copy[2][1]
    self.Face4[2][2] = Face4Copy[2][0]
    self.Face4[2][1] = Face4Copy[1][0]
    self.Face4[2][0] = Face4Copy[0][0]
    self.Face4[1][0] = Face4Copy[0][1]

elif Movement == "B": #back face to left 
    self.Moves.append("B")

    self.Face5[0][0] = Face2Copy[0][2]#
    self.Face5[0][1] = Face2Copy[1][2]#
    self.Face5[0][2] = Face2Copy[2][2]#

    self.Face6[2][0] = Face4Copy[0][0]#
    self.Face6[2][1] = Face4Copy[1][0]#
    self.Face6[2][2] = Face4Copy[2][0]#

    self.Face2[0][2] = Face6Copy[2][2]#
    self.Face2[1][2] = Face6Copy[2][1]#
    self.Face2[2][2] = Face6Copy[2][0]#

    self.Face4[0][0] = Face5Copy[0][2]#
    self.Face4[1][0] = Face5Copy[0][1]#
    self.Face4[2][0] = Face5Copy[0][0]#

    #clockwise face 3 
    self.Face3[0][0] = Face3Copy[2][0]
    self.Face3[0][1] = Face3Copy[1][0]
    self.Face3[0][2] = Face3Copy[0][0]
    self.Face3[1][2] = Face3Copy[0][1]
    self.Face3[2][2] = Face3Copy[0][2]
    self.Face3[2][1] = Face3Copy[1][2]
    self.Face3[2][0] = Face3Copy[2][2]
    self.Face3[1][0] = Face3Copy[2][1]

elif Movement == "Bi": #back face to right
    self.Moves.append("Bi")

    self.Face5[0][0] = Face4Copy[2][0]#
    self.Face5[0][1] = Face4Copy[1][0]#
    self.Face5[0][2] = Face4Copy[0][0]#

    self.Face6[2][0] = Face2Copy[2][2]#
    self.Face6[2][1] = Face2Copy[1][2]#
    self.Face6[2][2] = Face2Copy[0][2]#

    self.Face2[0][2] = Face5Copy[0][0]#
    self.Face2[1][2] = Face5Copy[0][1]#
    self.Face2[2][2] = Face5Copy[0][2]#

    self.Face4[0][0] = Face6Copy[2][0]#
    self.Face4[1][0] = Face6Copy[2][1]#
    self.Face4[2][0] = Face6Copy[2][2]#

    #anti clock face 3 
    self.Face3[0][0] = Face3Copy[0][2]
    self.Face3[0][1] = Face3Copy[1][2]
    self.Face3[0][2] = Face3Copy[2][2]
    self.Face3[1][2] = Face3Copy[2][1]
    self.Face3[2][2] = Face3Copy[2][0]
    self.Face3[2][1] = Face3Copy[1][0]
    self.Face3[2][0] = Face3Copy[0][0]
    self.Face3[1][0] = Face3Copy[0][1]

elif Movement == "D": #bottom right 
    self.Moves.append("D")
    for i in range(GRID_SIZE):
        self.Face1[2][i] = Face4Copy[2][i]#
        self.Face2[2][i] = Face1Copy[2][i]#
        self.Face3[2][i] = Face2Copy[2][i]#
        self.Face4[2][i] = Face3Copy[2][i]#

    #face 6 clockwise 
    self.Face6[0][0] = Face6Copy[2][0]
    self.Face6[0][1] = Face6Copy[1][0]
    self.Face6[0][2] = Face6Copy[0][0]
    self.Face6[1][2] = Face6Copy[0][1]
    self.Face6[2][2] = Face6Copy[0][2]
    self.Face6[2][1] = Face6Copy[1][2]
    self.Face6[2][0] = Face6Copy[2][2]
    self.Face6[1][0] = Face6Copy[2][1]

elif Movement == "Di": #bottom left 
    self.Moves.append("Di")
    for i in range(GRID_SIZE):
        self.Face1[2][i] = Face2Copy[2][i]#
        self.Face2[2][i] = Face3Copy[2][i]#
        self.Face3[2][i] = Face4Copy[2][i]#
        self.Face4[2][i] = Face1Copy[2][i]#

    #face 6 anti clock 
    self.Face6[0][0] = Face6Copy[0][2]
    self.Face6[0][1] = Face6Copy[1][2]
    self.Face6[0][2] = Face6Copy[2][2]
    self.Face6[1][2] = Face6Copy[2][1]
    self.Face6[2][2] = Face6Copy[2][0]
    self.Face6[2][1] = Face6Copy[1][0]
    self.Face6[2][0] = Face6Copy[0][0]
    self.Face6[1][0] = Face6Copy[0][1]

elif Movement == "F": #front right 
    self.Moves.append("F")

    self.Face5[2][0] = Face4Copy[2][2]#
    self.Face5[2][1] = Face4Copy[1][2]#
    self.Face5[2][2] = Face4Copy[0][2]#

    self.Face2[0][0] = Face5Copy[2][0]#
    self.Face2[1][0] = Face5Copy[2][1]#
    self.Face2[2][0] = Face5Copy[2][2]#

    self.Face4[0][2] = Face6Copy[0][0]#
    self.Face4[1][2] = Face6Copy[0][1]#
    self.Face4[2][2] = Face6Copy[0][2]#

    self.Face6[0][0] = Face2Copy[2][0]#
    self.Face6[0][1] = Face2Copy[1][0]#
    self.Face6[0][2] = Face2Copy[0][0]#

    #face 1 clockwise 
    self.Face1[0][0] = Face1Copy[2][0]
    self.Face1[0][1] = Face1Copy[1][0]
    self.Face1[0][2] = Face1Copy[0][0]
    self.Face1[1][2] = Face1Copy[0][1]
    self.Face1[2][2] = Face1Copy[0][2]
    self.Face1[2][1] = Face1Copy[1][2]
    self.Face1[2][0] = Face1Copy[2][2]
    self.Face1[1][0] = Face1Copy[2][1]

elif Movement == "Fi": #front left
    self.Moves.append("Fi")

    self.Face5[2][0] = Face2Copy[0][0]#
    self.Face5[2][1] = Face2Copy[1][0]#
    self.Face5[2][2] = Face2Copy[2][0]#

    self.Face2[0][0] = Face6Copy[0][2]#
    self.Face2[1][0] = Face6Copy[0][1]#
    self.Face2[2][0] = Face6Copy[0][0]#

    self.Face4[0][2] = Face5Copy[2][2]#
    self.Face4[1][2] = Face5Copy[2][1]#
    self.Face4[2][2] = Face5Copy[2][0]#

    self.Face6[0][0] = Face4Copy[0][2]#
    self.Face6[0][1] = Face4Copy[1][2]#
    self.Face6[0][2] = Face4Copy[2][2]#

    #face 1 anti 
    self.Face1[0][0] = Face1Copy[0][2]
    self.Face1[0][1] = Face1Copy[1][2]
    self.Face1[0][2] = Face1Copy[2][2]
    self.Face1[1][2] = Face1Copy[2][1]
    self.Face1[2][2] = Face1Copy[2][0]
    self.Face1[2][1] = Face1Copy[1][0]
    self.Face1[2][0] = Face1Copy[0][0]
    self.Face1[1][0] = Face1Copy[0][1]

elif Movement == "U": #top left 
    self.Moves.append("U")
    for i in range(GRID_SIZE):
        self.Face1[0][i] = Face2Copy[0][i]#
        self.Face2[0][i] = Face3Copy[0][i]#
        self.Face3[0][i] = Face4Copy[0][i]#
        self.Face4[0][i] = Face1Copy[0][i]#

    #face 5 clockwise 
    self.Face5[0][0] = Face5Copy[2][0]
    self.Face5[0][1] = Face5Copy[1][0]
    self.Face5[0][2] = Face5Copy[0][0]
    self.Face5[1][2] = Face5Copy[0][1]
    self.Face5[2][2] = Face5Copy[0][2]
    self.Face5[2][1] = Face5Copy[1][2]
    self.Face5[2][0] = Face5Copy[2][2]
    self.Face5[1][0] = Face5Copy[2][1]

elif Movement == "Ui": #top right
    self.Moves.append("Ui")
    for i in range(GRID_SIZE):
        self.Face1[0][i] = Face4Copy[0][i]#
        self.Face2[0][i] = Face1Copy[0][i]#
        self.Face3[0][i] = Face2Copy[0][i]#
        self.Face4[0][i] = Face3Copy[0][i]#

    #face 5 anti
    self.Face5[0][0] = Face5Copy[0][2]
    self.Face5[0][1] = Face5Copy[1][2]
    self.Face5[0][2] = Face5Copy[2][2]
    self.Face5[1][2] = Face5Copy[2][1]
    self.Face5[2][2] = Face5Copy[2][0]
    self.Face5[2][1] = Face5Copy[1][0]
    self.Face5[2][0] = Face5Copy[0][0]
    self.Face5[1][0] = Face5Copy[0][1]

elif Movement == "M":
    self.Moves.append("M")
    for i in range(GRID_SIZE):
        self.Face1[1][i] = Face2Copy[1][i]#
        self.Face2[1][i] = Face3Copy[1][i]#
        self.Face3[1][i] = Face4Copy[1][i]#
        self.Face4[1][i] = Face1Copy[1][i]#
