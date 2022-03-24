from sys import winver
import cv2
import numpy as np
import ColorRanges as CR
import Solver
from tkinter import * 
import threading
from PIL import Image, ImageTk


CELL_SIZE = 100
GRID_SIZE = 3




CellCenters = [[["x","y"] for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]


def Debug(Frame):
    hsvim = cv2.cvtColor(Frame, cv2.COLOR_BGR2HSV)
    Mask = cv2.inRange(hsvim, CR.LOWER_RED_RANGE, CR.UPPER_RED_RANGE)
    cv2.imshow("Mask", Mask)

def DrawScanGrid(Image, H, W, FaceToScan):
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            StartingX, StartingY = int(H/3), int(W*0.15)
            x1 , y1 = (x*CELL_SIZE)+StartingX, y*CELL_SIZE +StartingY
            cv2.rectangle(Image,(x1,y1),(x1+CELL_SIZE, y1+CELL_SIZE),(255,0,0),2) #create cell in each of the 3^2 locations 
            CellCenters[x][y] = [int((x1+x1+CELL_SIZE)/2),int((y1+y1+CELL_SIZE)/2)] #add the center of each cell to the list 
            
    cv2.putText(Image,f"Current Face: {FaceToScan}", (int(H*0.05),int(W*0.1)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

def DrawScan(Face):
    Canvas = np.zeros((CELL_SIZE*GRID_SIZE,CELL_SIZE*GRID_SIZE,3), np.uint8)
    ScannedFace = Solver.Face1

    if Face == 1:
        ScannedFace = Solver.Face1
    elif Face == 2:
        ScannedFace = Solver.Face2
    elif Face == 3:
        ScannedFace = Solver.Face3
    elif Face == 4:
        ScannedFace = Solver.Face4
    elif Face == 5:
        ScannedFace = Solver.Face5
    elif Face == 6:
        ScannedFace = Solver.Face6
    


    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            x1 , y1 = x*CELL_SIZE, y*CELL_SIZE

        
            if ScannedFace[y][x] == "N":
                cv2.rectangle(Canvas,(x1,y1),(x1+CELL_SIZE, y1+CELL_SIZE), CR.NONE, -1)
                cv2.rectangle(Canvas,(x1,y1),(x1+CELL_SIZE, y1+CELL_SIZE), (0,0,0), 2)
            elif ScannedFace[y][x] == "W":
                cv2.rectangle(Canvas,(x1,y1),(x1+CELL_SIZE, y1+CELL_SIZE), CR.WHITE, -1)
                cv2.rectangle(Canvas,(x1,y1),(x1+CELL_SIZE, y1+CELL_SIZE), (0,0,0), 2)
            elif ScannedFace[y][x] == "G":
                cv2.rectangle(Canvas,(x1,y1),(x1+CELL_SIZE, y1+CELL_SIZE), CR.GREEN, -1)
                cv2.rectangle(Canvas,(x1,y1),(x1+CELL_SIZE, y1+CELL_SIZE), (0,0,0), 2)
            elif ScannedFace[y][x] == "Y":
                cv2.rectangle(Canvas,(x1,y1),(x1+CELL_SIZE, y1+CELL_SIZE), CR.YELLOW, -1)
                cv2.rectangle(Canvas,(x1,y1),(x1+CELL_SIZE, y1+CELL_SIZE), (0,0,0), 2)
            elif ScannedFace[y][x] == "B":
                cv2.rectangle(Canvas,(x1,y1),(x1+CELL_SIZE, y1+CELL_SIZE), CR.BLUE, -1)
                cv2.rectangle(Canvas,(x1,y1),(x1+CELL_SIZE, y1+CELL_SIZE), (0,0,0), 2)
            elif ScannedFace[y][x] == "R":
                cv2.rectangle(Canvas,(x1,y1),(x1+CELL_SIZE, y1+CELL_SIZE), CR.RED, -1)
                cv2.rectangle(Canvas,(x1,y1),(x1+CELL_SIZE, y1+CELL_SIZE), (0,0,0), 2)
            elif ScannedFace[y][x] == "O":
                cv2.rectangle(Canvas,(x1,y1),(x1+CELL_SIZE, y1+CELL_SIZE), CR.ORANGE, -1)
                cv2.rectangle(Canvas,(x1,y1),(x1+CELL_SIZE, y1+CELL_SIZE), (0,0,0), 2)
                
    cv2.imshow("Cube Scan", Canvas) #show screen with scan colors 
    cv2.imwrite(f"Faces\\Face{Face}.png", Canvas)

def CheckCellColors(Image, ImageFaceNum):
    CurrentFace = [["N" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            HSVImage = cv2.cvtColor(Image, cv2.COLOR_BGR2HSV)

            for ColorNum in range(6):  #cicle every color on every cordinate to find macth
                CurrentLowerColor = None
                CurrentUpperColor = None
                CurrentColor = None

                if ColorNum == 0:
                    CurrentLowerColor = CR.LOWER_WHITE_RANGE
                    CurrentUpperColor = CR.UPPER_WHITE_RANGE
                    CurrentColor = "W"
                elif ColorNum == 1:
                    CurrentLowerColor = CR.LOWER_GREEN_RANGE
                    CurrentUpperColor = CR.UPPER_GREEN_RANGE
                    CurrentColor = "G"
                elif ColorNum == 2:
                    CurrentLowerColor = CR.LOWER_YELLOW_RANGE
                    CurrentUpperColor = CR.UPPER_YELLOW_RANGE
                    CurrentColor = "Y"
                elif ColorNum == 3:
                    CurrentLowerColor = CR.LOWER_BLUE_RANGE
                    CurrentUpperColor = CR.UPPER_BLUE_RANGE
                    CurrentColor = "B"
                elif ColorNum == 4:
                    CurrentLowerColor = CR.LOWER_RED_RANGE
                    CurrentUpperColor = CR.UPPER_RED_RANGE
                    CurrentColor = "R"
                elif ColorNum == 5:
                    CurrentLowerColor = CR.LOWER_ORANGE_RANGE
                    CurrentUpperColor = CR.UPPER_ORANGE_RANGE
                    CurrentColor = "O"

                Mask = cv2.inRange(HSVImage, CurrentLowerColor, CurrentUpperColor)  
                #MaskResult = cv2.bitwise_and(Image, Image, mask=Mask)  image tih the mask actual detected color not only white
                CenterX = CellCenters[x][y][0]
                CenterY = CellCenters[x][y][1]

                if Mask[CenterY, CenterX] == 255:
                    #print(f"Color {CurrentColor} at cell {x,y}")
                    CurrentFace[y][x] = CurrentColor #ADD COLOR CODE TO 2D LIST OF CUBE FACE 
                    break

            #cv2.circle(Frame,(CellCenters[x][y][0],CellCenters[x][y][1]),3,(255,0,0),-1)

    if ImageFaceNum == 1:
        Solver.Face1 = CurrentFace
    elif ImageFaceNum == 2:
        Solver.Face2 = CurrentFace
    elif ImageFaceNum == 3:
        Solver.Face3 = CurrentFace
    elif ImageFaceNum == 4:
        Solver.Face4 = CurrentFace
    elif ImageFaceNum == 5:
        Solver.Face5 = CurrentFace
    elif ImageFaceNum == 6:
        Solver.Face6 = CurrentFace

Webcam = cv2.VideoCapture(0)

def Main():

    
        
    Window = Tk()

    

    def UpdateScreen(): #move while tru loop into here 
        
        

        FaceNum = 1
    
        
        Succes, Frame = Webcam.read()
        #Frame = cv2.imread("Images\\WebcamImage.png") #---debuggin image 
        FrameHeight, FrameWidth ,_ = 400,400,1
        #Frame = cv2.flip(Frame, 1)



        DrawScanGrid(Frame,FrameHeight,FrameWidth, FaceNum)

        
    
            
        
        cv2.imshow("Webcam", Frame) #show frame "webcam"
        ###check imputs ###
        k = cv2.waitKey(1)
        if k == 27: #esc key to exit
            #cv2.imwrite("test.png", Frame)
            #break
            pass

        if k == ord('s') or k == ord("S"):
            CheckCellColors(Frame, FaceNum)
            DrawScan(FaceNum)
            FaceNum += 1


        if k == ord('r') or k == ord("R"):
            
            print("1")
            for row1 in Solver.Face1:
                print(row1)
            print("2")
            for row1 in Solver.Face2:
                print(row1)
            print("3")
            for row1 in Solver.Face3:
                print(row1)
            print("4")
            for row1 in Solver.Face4:
                print(row1)
            print("5")
            for row1 in Solver.Face5:
                print(row1)
            print("6")
            for row1 in Solver.Face6:
                print(row1)



        if k == ord('t') or k == ord("T"):
            DrawScan(1)  #this will display the saved face 1 
                

            


        Webcam.release()
        cv2.destroyAllWindows


        Window.after(100, UpdateScreen)

    def helloCallBack():
        print( "Hello Python", "Hello World")



    B = Button(Window, text ="Hello", command = helloCallBack)
    B.pack()

    Window.after(100, UpdateScreen)
    Window.mainloop()



    


if __name__ == "__main__":
    Main()

