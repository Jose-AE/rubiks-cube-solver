import numpy as np

#Scan display colors 
#NONE = (244,0,255)
NONE = (0,0,0)

WHITE = (255,255,255)
GREEN = (0,255,114)
YELLOW = (13,207,255)
BLUE = (255,0,0)
RED = (0,0,255)
ORANGE = (13,138,255)


#image color ranges
#(hMin = 0 , sMin = 0, vMin = 168), (hMax = 179 , sMax = 46, vMax = 255)--C
LOWER_WHITE_RANGE = np.array([0,0,168])
UPPER_WHITE_RANGE = np.array([179,46,255])

#(hMin = 47 , sMin = 167, vMin = 0), (hMax = 82 , sMax = 255, vMax = 255)--c
LOWER_GREEN_RANGE = np.array([47,168,0])
UPPER_GREEN_RANGE = np.array([82,255,255])

#(hMin = 14 , sMin = 71, vMin = 167), (hMax = 42 , sMax = 214, vMax = 255)--c
LOWER_YELLOW_RANGE = np.array([14,71,167])
UPPER_YELLOW_RANGE = np.array([42,214,255])

#(hMin = 80 , sMin = 201, vMin = 0), (hMax = 129 , sMax = 255, vMax = 255)-c
LOWER_BLUE_RANGE = np.array([80,201,0])
UPPER_BLUE_RANGE = np.array([129,255,255])

#(hMin = 166 , sMin = 0, vMin = 0), (hMax = 179 , sMax = 255, vMax = 255)--conf
LOWER_RED_RANGE = np.array([166,0,0])
UPPER_RED_RANGE = np.array([179,255,255])

#(hMin = 0 , sMin = 170, vMin = 187), (hMax = 31 , sMax = 255, vMax = 255)
LOWER_ORANGE_RANGE = np.array([0,170,187])
UPPER_ORANGE_RANGE = np.array([31,255,255])


