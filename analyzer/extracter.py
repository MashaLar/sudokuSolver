# extracter.py file
from imutils.perspective import four_point_transform
from skimage.segmentation import clear_border
import numpy as np
import imutils
import cv2

MAX_COLOR_VALUE = 255

def process_image_binary(image):
    blurred = cv2.GaussianBlur(image, (7, 7), 3)

    thresh = cv2.adaptiveThreshold(blurred, MAX_COLOR_VALUE,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    thresh = cv2.bitwise_not(thresh)
    return thresh

def get_largest_contour(image):
    thresh = process_image_binary(image)

    contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    return contours
    
def get_box_contour(image):
    contours = get_largest_contour(image)
    boxContour = None

    for c in contours:
        approx = cv2.approxPolyDP(c, 0.02 * cv2.arcLength(c, True), True)
        if len(approx) == 4:
            boxContour = approx
            break
    
    if boxContour is None:
        raise Exception(("Can't find 4 points for contour!"))

    return boxContour  

def find_puzzle(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    puzzleContour = get_box_contour(gray)
   
    # apply a four point perspective transform to obtain a top-down bird's eye view
    puzzleRGB = four_point_transform(image, puzzleContour.reshape(4, 2))
    puzzleGray = four_point_transform(gray, puzzleContour.reshape(4, 2))

    return (puzzleRGB, puzzleGray)
    
def process_image_otsu(cell): 
    thresh = cv2.threshold(cell, 0, MAX_COLOR_VALUE,
        cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    thresh = clear_border(thresh)
    return thresh
    
def get_contour(thresh, cell): 
    contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    if len(contours) == 0:
        return None
    
    mask = np.zeros(thresh.shape, dtype="uint8")
    cv2.drawContours(mask, [max(contours, key=cv2.contourArea)], -1, MAX_COLOR_VALUE, -1)
    return mask

def percent_filled(thresh, mask): 
    (h, w) = thresh.shape
    percentFilled = cv2.countNonZero(mask) / float(w * h)
    
    if percentFilled < 0.03:
        return None

    digit = cv2.bitwise_and(thresh, thresh, mask=mask)
    return digit
    
def extract_digit(cell):
    digit = None
    thresh = process_image_otsu(cell)
    mask = get_contour(thresh, cell)
  
    if mask is None:
        return digit

    digit =  percent_filled(thresh, mask)
    return digit