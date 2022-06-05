# solver.py file
from sudoku import Sudoku
import analyzer.extracter as extr
import analyzer.drawer as dr
import analyzer.setter as st
import argparse
import imutils
import cv2

modelPath = "./model/output/MODEL.h5"
#imagePath = "./images/su.jpg"
#image = imutils.resize(cv2.imread(imagePath), width=600)
#(puzzleImage, box) = extr.find_puzzle(image)

#(board, cellLocations) = st.read_board(box, modelPath)

#print("[INFO] OCR'd Sudoku board:")
#puzzle = Sudoku(3, 3, board=board.tolist())
#puzzle.show()

#print("[INFO] solving Sudoku puzzle...")
#solution = Sudoku(3, 3, board=board.tolist()).solve()
#solution.show_full()

#dr.draw_on_image(cellLocations, solution.board, puzzleImage)

#cv2.imshow("Sudoku Result", puzzleImage)
#cv2.waitKey(0)

def solve_on_image(image):
    (puzzleImage, box) = extr.find_puzzle(image)
    
    (board, cellLocations) = st.read_board(box, modelPath)
    
    print("[INFO] OCR'd Sudoku board:")
    puzzle = Sudoku(3, 3, board=board.tolist())
    puzzle.show()
    
    print("[INFO] solving Sudoku puzzle...")
    solution = Sudoku(3, 3, board=board.tolist()).solve()
    solution.show_full()
    
    dr.draw_on_image(cellLocations, solution.board, puzzleImage)
    return (solution, puzzleImage)

def get_board_from_image(imagePath):
    image = imutils.resize(cv2.imread(imagePath), width=600)
    (puzzleImage, box) = extr.find_puzzle(image)
    
    (board, cellLocations) = st.read_board(box, modelPath)
    
    return board.tolist()