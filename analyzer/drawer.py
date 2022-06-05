# drawer.py file
import cv2

def draw_on_image(cells, board, image):
    for (cRow, bRow) in zip(cells, board):
    	for (location, number) in zip(cRow, bRow):
    		x1, y1, x2, y2 = location
            
    		textX = int((x2 - x1) * 0.33)
    		textY = int((y2 - y1) * -0.2)
    		textX += x1
    		textY += y2
    
    		cv2.putText(image, str(number), (textX, textY),
    			cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)