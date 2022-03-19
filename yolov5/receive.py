import detect as dt
import cv2

generator = dt.run_detect()
image = ''
#print(vars(fuck_you))
while True:
    image= next(generator)
    cv2.imshow("Fuck", image)
    
