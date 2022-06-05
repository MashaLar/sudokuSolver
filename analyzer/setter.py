# setter.py file
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import analyzer.extracter as extr
import numpy as np
import argparse
import imutils
import cv2

def step_forward(iStep, jStep, i, j):
    x1 = i * iStep
    y1 = j * jStep
    x2 = (i + 1) * iStep
    y2 = (j + 1) * jStep
    return (x1, y1, x2, y2)

def read_board(box, modelPath):
    model = load_model(modelPath)
    puzzle = np.zeros((9, 9), dtype="int")
    iStep = box.shape[1] // 9
    jStep = box.shape[0] // 9
    cellLocations = []
    
    for j in range(0, 9):
    	row = []
    	for i in range(0, 9):
    		x1, y1,	x2,	y2 = step_forward(iStep, jStep, i, j)
            
    		row.append((x1, y1, x2, y2))
    		number = extr.extract_digit(box[y1:y2, x1:x2])
            
    		if number is not None:
    			numImage = cv2.resize(number, (28, 28))
    			numImage = img_to_array(numImage.astype("float") / 255.0)
    			numImage = np.expand_dims(numImage, axis=0)
                
    			puzzle[j, i] = model.predict(numImage).argmax(axis=1)[0]
                
    	cellLocations.append(row)
    return (puzzle, cellLocations)