import cv2
import numpy as np
import Hand_guesture as htm
from collections import Counter
print(htm)

import detect as dt
##from Detect_uploaded_video import detection

import win32com.client as wincl
#global variables

speak = wincl.Dispatch("SAPI.SpVoice")

location = "C:/Users/PAVILION/AppData/Local/Programs/Python/Python37/Drowsiness_detect/yolov5/"

generator = dt.run_detect()
frame = ''
class_name = ''
sequence = []
sentence = []
predictions = []
threshold = 0.5

colors = [(245,117,16), (117,245,16), (16,117,245)]

touched = False
count = 0

let = ""
text = ''
final_text = ""
space = False

hand_sequence = []
letter_sequence = []
sequence = []
sentence = []
predictions = []
threshold = 0.5
colors = [(245,117,16), (117,245,16), (16,117,245)]

def most_freq(arr):
    occur = Counter(arr)
    return occur.most_common(1)[0][0]


def prob_viz(res, actions, input_frame, colors):
    output_frame = input_frame.copy()
    for num, prob in enumerate(res):
        cv2.rectangle(output_frame, (0,60+num*40), (int(prob*100), 90+num*40), colors[num], -1)
        cv2.putText(output_frame, actions[num], (0, 85+num*40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
        
    return output_frame

cap = cv2.VideoCapture(0)
detector = htm.handDetector(detectionCon=0.75)

tipIds = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
#keypoints = run()
while True:
    
    
    frame, class_name = next(generator)
    #print(class_name)
    #ret, frame = cap.read()
    img = detector.findHands(frame)
    lmList = detector.findPosition(img, draw=False)
    hand = detector.handName(img)
##    print(count)

    ## Action Sequence  ##
    
    if touched == False:
       
        count += 1
        
        #print(class_name)
        
       
        #print(results)
        
        # Draw landmarks
        
##        sequence.append(keypoints)
##        sequence = sequence[-30:]
##        
##        if len(sequence) == 30:
##            #res = model.predict(np.expand_dims(sequence, axis=0))[0]
##            #print(np.argmax(res))
##            #print(actions[np.argmax(res)])
##            predictions.append(np.argmax(res))
##            #print(predictions)
##            #print(np.unique(predictions[-10:]))
##        #3. Viz logic
##            if np.unique(predictions[-10:])[0]==np.argmax(res): 
##                if res[np.argmax(res)] > threshold:
##                    
##                    #print(sentence)
##                    if len(sentence) > 0: 
##                        if actions[np.argmax(res)] != sentence[-1]:
##                            speak.Speak(actions[np.argmax(res)])
##                            sentence.append(actions[np.argmax(res)])
##                    else:
##                        sentence.append(actions[np.argmax(res)])
##                        speak.Speak(actions[np.argmax(res)])
##
##            if len(sentence) > 5: 
##                sentence = sentence[-5:]
##                
##                #print(sentence)
##            # Viz probabilities
##            image = prob_viz(res, actions, image, colors)
        
        cv2.rectangle(frame, (0,0), (640, 40), (245, 117, 16), -1)
        cv2.putText(frame, ''.join(class_name), (3,30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.rectangle(frame, (280,50), (400,100), (255,0,0), 2)
        
    ## Alphabets ##
        
    if touched == True:
        hand_sequence.append(hand)
        if len(hand_sequence)>=5:
            #print(hand_sequence[-5:])
            hand_final = most_freq(hand_sequence)
            #print(hand_final)
            if hand_final == "Right":
                speak.Speak(final_text)
                hand_sequence = []
                cv2.rectangle(img, (280,50), (400,100), (0,255,0), -1)
                count += 1
            hand_sequence = hand_sequence[-5:]
        cv2.rectangle(img, (280,50), (400,100), (0,255,0), -1)
        count += 1
        if len(lmList) > 0 and hand == "Left":
            if lmList[4][1] > lmList[6][1] and lmList[5][2] < lmList[8][2] and lmList[9][2] < lmList[12][2] and lmList[13][2] < lmList[16][2] and lmList[17][2] < lmList[20][2] and lmList[4][2] < lmList[5][2]:
                text = "A"
            elif lmList[5][1] < lmList[4][1] and lmList[8][2] < lmList[7][2] and lmList[12][2] < lmList[11][2] and lmList[16][2] < lmList[15][2] and lmList[20][2] < lmList[19][2]:
                text = " "
            elif lmList[5][1] > lmList[4][1] and lmList[8][2] < lmList[7][2] and lmList[12][2] < lmList[11][2] and lmList[16][2] < lmList[15][2] and lmList[20][2] < lmList[19][2]:
                text = "B"
            #elif lmList[8][1] > lmList[7][1] and lmList[6][2] < lmList[10][2]:
                #text = "P"
            elif lmList[8][1] > lmList[7][1] and lmList[12][1] > lmList[11][1] and lmList[16][1] < lmList[14][1] and lmList[0][1] < lmList[5][1] and lmList[4][2] > lmList[10][2] and lmList[0][1] < lmList[17][1]: 
                text = "H"
            elif lmList[16][1] > lmList[9][1] and lmList[11][2] < lmList[12][2] and (lmList[5][1] and lmList[9][1] and lmList[13][1] and lmList[17][1] ) < lmList[4][1] and (lmList[5][1] and lmList[9][1] and lmList[13][1] and lmList[17][1] ) > lmList[0][1] and lmList[4][2] > lmList[12][2]:
                text = "C"
            elif lmList[6][2] > lmList[8][2] and lmList[10][2] < lmList[12][2] and lmList[14][2] < lmList[16][2] and lmList[18][2] < lmList[20][2] and lmList[4][1] <= lmList[5][1]:
                text = "D"

            elif lmList[6][2] < lmList[8][2] and lmList[10][2] < lmList[12][2] and lmList[14][2] < lmList[16][2] and lmList[18][2] < lmList[20][2] and lmList[4][2] > lmList[7][2] and lmList[4][1] < lmList[8][1] :
                text = "E"
            elif lmList[7][2] < lmList[4][2] and lmList[8][2] > lmList[6][2] and lmList[4][1] < lmList[8][1] and lmList[12][2] < lmList[11][2] and lmList[16][2] < lmList[15][2] and lmList[20][2] < lmList[19][2]:
                text = "F"
            elif lmList[8][1] > lmList[7][1] and lmList[12][1] < lmList[11][1] and lmList[0][1] < lmList[5][1] and lmList[4][2] > lmList[6][2] and lmList[0][1] < lmList[17][1]: 
                text = "G"
            
            elif lmList[5][2] < lmList[8][2] and lmList[9][2] < lmList[12][2] and lmList[13][2] < lmList[16][2] and lmList[19][2] > lmList[20][2] and lmList[19][2] > lmList[6][2] and lmList[4][1] < lmList[8][1]:
                text = "J"
            elif lmList[5][2] < lmList[8][2] and lmList[9][2] < lmList[12][2] and lmList[13][2] < lmList[16][2] and lmList[19][2] > lmList[20][2] and lmList[4][1] < lmList[8][1]:
                text = "I"
            
            elif lmList[6][1] < lmList[4][1] and lmList[4][1] < lmList[10][1] and lmList[15][2] < lmList[16][2] and lmList[20][2] > lmList[19][2]: 
                text = "K"
            elif lmList[6][2] > lmList[8][2] and lmList[10][2] < lmList[12][2] and lmList[14][2] < lmList[16][2] and lmList[18][2] < lmList[20][2] and lmList[4][1] >lmList[5][1] and lmList[4][2] >lmList[5][2] and lmList[4][1] >lmList[3][1] and lmList[0][1] > lmList[17][1]:
                text = "L"
            elif lmList[14][2] < lmList[4][2] and lmList[5][2] < lmList[8][2] and lmList[9][2] < lmList[12][2] and lmList[13][2] < lmList[16][2] and lmList[17][2] < lmList[20][2] and lmList[4][1] < lmList[5][1] and lmList[4][2] > lmList[6][2] and lmList[16][2] > lmList[4][2]:
                text = "M"
            elif lmList[14][2] > lmList[4][2] and lmList[5][2] < lmList[8][2] and lmList[9][2] < lmList[12][2] and lmList[13][2] < lmList[16][2] and lmList[17][2] < lmList[20][2] and lmList[4][1] < lmList[5][1] and lmList[4][2] > lmList[6][2] and lmList[16][2] > lmList[4][2]:
                text = "N"
            elif lmList[16][1] > lmList[9][1] and lmList[11][2] < lmList[12][2] and (lmList[5][1] and lmList[9][1] and lmList[13][1] and lmList[17][1] ) < lmList[4][1] and lmList[4][2] < lmList[12][2]:
                text = "O"
            
            else:
                text = "None"

            
            letter_sequence.append(text)
            final_text = final_text[-33:]
            if len(letter_sequence) >= 10:
                
                let = most_freq(letter_sequence)
                #print(let)
                if let != 'None':
                    hovered = False
                    final_text += let
                    letter_sequence = []
        
                        
##                    print(final_text)
        cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(text), (45, 375), cv2.FONT_HERSHEY_PLAIN,10, (255, 0, 0), 10)

        
        cv2.rectangle(img, (0,0), (640, 40), (245, 117, 16), -1)
        cv2.putText(img, ''.join(final_text), (3,30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        text = ""
    if len(lmList) > 0:
        
##        print(lmList[8])
        if lmList[8][1] >= 280 and lmList[8][1] <= 400 and lmList[8][2] >= 60 and lmList[8][2] <= 90 and count > 20:
            #cv2.rectangle(img, (320,240), (370,290), (0,255,0), -1)
            
            if touched == False:
                touched = True
                count = 0
                
        if lmList[8][1] >= 280 and lmList[8][1] <= 400 and lmList[8][2] >= 60 and lmList[8][2] <= 90 and touched == True and count > 100:
            if touched == True:
                touched = False
                count = 0
    
    cv2.imshow("Detect", img)
    cv2.waitKey(1)


cap.release()
cv2.destroyAllWindows()
    
