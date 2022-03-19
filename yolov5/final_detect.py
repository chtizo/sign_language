import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2
import detect as dt
import os
import numpy as np
import Hand_guesture as htm
import win32com.client as wincl
#import detect as dt


##generator = dt.run_detect()
##image = ''
##
##let = ""
##final_text = ""
##space = False
##
##worker_check = False
##
##hand_sequence = []
##letter_sequence = []
##sequence = []
##sentence = []
##predictions = []
##threshold = 0.5
##colors = [(245,117,16), (117,245,16), (16,117,245)]
##


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.VBL = QVBoxLayout()

        self.FeedLabel = QLabel()
        self.VBL.addWidget(self.FeedLabel)

        self.CancelBTN = QPushButton("Alphabet")
        self.CancelBTN.clicked.connect(self.Alphabet)
        self.VBL.addWidget(self.CancelBTN)

        self.Worker1 = Worker1()

        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.setLayout(self.VBL)

    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))
        
    def most_freq(arr):
        occur = Counter(arr)
        return occur.most_common(1)[0][0]

    def Alphabet(self):

##        if worker_check:
        self.Worker1.stop()
##        
##        cap = cv2.VideoCapture(0)
##        detector = htm.handDetector(detectionCon=0.75)
##
##        tipIds = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
##
##        while True:
##            ret, frame = cap.read()
##            img = detector.findHands(frame)
##            lmList = detector.findPosition(img, draw=False)
##            hand = detector.handName(img)
##            if len(lmList) > 0:
##                if lmList[4][1] > lmList[6][1] and lmList[5][2] < lmList[8][2] and lmList[9][2] < lmList[12][2] and lmList[13][2] < lmList[16][2] and lmList[17][2] < lmList[20][2] and lmList[4][2] < lmList[5][2]:
##                    text = "A"
##                elif lmList[5][1] < lmList[4][1] and lmList[8][2] < lmList[7][2] and lmList[12][2] < lmList[11][2] and lmList[16][2] < lmList[15][2] and lmList[20][2] < lmList[19][2]:
##                    text = " "
##                elif lmList[5][1] > lmList[4][1] and lmList[8][2] < lmList[7][2] and lmList[12][2] < lmList[11][2] and lmList[16][2] < lmList[15][2] and lmList[20][2] < lmList[19][2]:
##                    text = "B"
##                #elif lmList[8][1] > lmList[7][1] and lmList[6][2] < lmList[10][2]:
##                    #text = "P"
##                elif lmList[8][1] > lmList[7][1] and lmList[12][1] > lmList[11][1] and lmList[16][1] < lmList[14][1] and lmList[0][1] < lmList[5][1] and lmList[4][2] > lmList[10][2] and lmList[0][1] < lmList[17][1]: 
##                    text = "H"
##                elif lmList[16][1] > lmList[9][1] and lmList[11][2] < lmList[12][2] and (lmList[5][1] and lmList[9][1] and lmList[13][1] and lmList[17][1] ) < lmList[4][1] and (lmList[5][1] and lmList[9][1] and lmList[13][1] and lmList[17][1] ) > lmList[0][1] and lmList[4][2] > lmList[12][2]:
##                    text = "C"
##                elif lmList[6][2] > lmList[8][2] and lmList[10][2] < lmList[12][2] and lmList[14][2] < lmList[16][2] and lmList[18][2] < lmList[20][2] and lmList[4][1] <= lmList[5][1]:
##                    text = "D"
##
##                elif lmList[6][2] < lmList[8][2] and lmList[10][2] < lmList[12][2] and lmList[14][2] < lmList[16][2] and lmList[18][2] < lmList[20][2] and lmList[4][2] > lmList[7][2] and lmList[4][1] < lmList[8][1] :
##                    text = "E"
##                elif lmList[7][2] < lmList[4][2] and lmList[8][2] > lmList[6][2] and lmList[4][1] < lmList[8][1] and lmList[12][2] < lmList[11][2] and lmList[16][2] < lmList[15][2] and lmList[20][2] < lmList[19][2]:
##                    text = "F"
##                elif lmList[8][1] > lmList[7][1] and lmList[12][1] < lmList[11][1] and lmList[0][1] < lmList[5][1] and lmList[4][2] > lmList[6][2] and lmList[0][1] < lmList[17][1]: 
##                    text = "G"
##                
##                elif lmList[5][2] < lmList[8][2] and lmList[9][2] < lmList[12][2] and lmList[13][2] < lmList[16][2] and lmList[19][2] > lmList[20][2] and lmList[19][2] > lmList[6][2] and lmList[4][1] < lmList[8][1]:
##                    text = "J"
##                elif lmList[5][2] < lmList[8][2] and lmList[9][2] < lmList[12][2] and lmList[13][2] < lmList[16][2] and lmList[19][2] > lmList[20][2] and lmList[4][1] < lmList[8][1]:
##                    text = "I"
##                
##                elif lmList[6][1] < lmList[4][1] and lmList[4][1] < lmList[10][1] and lmList[15][2] < lmList[16][2] and lmList[20][2] > lmList[19][2]: 
##                    text = "K"
##                elif lmList[6][2] > lmList[8][2] and lmList[10][2] < lmList[12][2] and lmList[14][2] < lmList[16][2] and lmList[18][2] < lmList[20][2] and lmList[4][1] >lmList[5][1] and lmList[4][2] >lmList[5][2] and lmList[4][1] >lmList[3][1] and lmList[0][1] > lmList[17][1]:
##                    text = "L"
##                elif lmList[14][2] < lmList[4][2] and lmList[5][2] < lmList[8][2] and lmList[9][2] < lmList[12][2] and lmList[13][2] < lmList[16][2] and lmList[17][2] < lmList[20][2] and lmList[4][1] < lmList[5][1] and lmList[4][2] > lmList[6][2] and lmList[16][2] > lmList[4][2]:
##                    text = "M"
##                elif lmList[14][2] > lmList[4][2] and lmList[5][2] < lmList[8][2] and lmList[9][2] < lmList[12][2] and lmList[13][2] < lmList[16][2] and lmList[17][2] < lmList[20][2] and lmList[4][1] < lmList[5][1] and lmList[4][2] > lmList[6][2] and lmList[16][2] > lmList[4][2]:
##                    text = "N"
##                elif lmList[16][1] > lmList[9][1] and lmList[11][2] < lmList[12][2] and (lmList[5][1] and lmList[9][1] and lmList[13][1] and lmList[17][1] ) < lmList[4][1] and lmList[4][2] < lmList[12][2]:
##                    text = "O"
##                
##                else:
##                    text = "None"
##
##                
##                letter_sequence.append(text)
##                final_text = final_text[-33:]
##                if len(letter_sequence) >= 50:
##                    
##                    let = self.most_freq(letter_sequence)
##                    #print(let)
##                    if let != 'None':
##                        hovered = False
##                        final_text += let
##                        letter_sequence = []
##            
##                            
##    ##                    print(final_text)
##            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
##            cv2.putText(img, str(text), (45, 375), cv2.FONT_HERSHEY_PLAIN,10, (255, 0, 0), 10)
##
##            
##            cv2.rectangle(img, (0,0), (640, 40), (245, 117, 16), -1)
##            cv2.putText(img, ''.join(final_text), (3,30), 
##                       cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    

class Worker1(QThread):

    ImageUpdate = pyqtSignal(QImage)
    
    def run(self):
        self.ThreadActive = True
        vc = cv2.VideoCapture(0)
        while self.ThreadActive:
            ret, frame = vc.read()
            
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Importage, 1)
                ConverToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConverToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
##            self.run_detect()

##    def run_detect(self):
##        
##        #im0= next(generator)
##        ret, frame = self.vc.read()
##        
##        if ret:
##            Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
##            FlippedImage = cv2.flip(Importage, 1)
##            ConverToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
##            Pic = ConverToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
##            self.ImageUpdate.emit(Pic)
                    
               
            
    def stop(self):
        self.Alphabet()
        self.quit()
   
   

if __name__== "__main__":
    App = QApplication(sys.argv)
    Root = MainWindow()
    Root.show()
    sys.exit(App.exec())
