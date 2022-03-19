location = "C:/Users/PAVILION/AppData/Local/Programs/Python/Python37/Drowsiness_detect/yolov5/"

##def detection(link, location):
    
    

def detection(link, location):
    import torch
    from matplotlib import pyplot as plt
    import numpy as np
    import cv2
    import os
    from GPUtil import showUtilization as gpu_usage
    import tensorflow as tf
    import shutil
    import json
   

    
    
    model = torch.hub.load('ultralytics/yolov5', 'custom', path= location + 'runs/train/exp27/weights/last.pt', force_reload=True)
    
    emotion = []
    state = []
    cap = cv2.VideoCapture(link)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    current_frame = 0
    
    frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
    print(frame_rate)
    time = total_frames/frame_rate
    while cap.isOpened():
        current_frame +=1
        current_time = current_frame/frame_rate
        #print((current_frame/total_frames)*100)
        ret, frame = cap.read()
        down_width = 640
        down_height = 480
        down_points = (down_width, down_height)

        resized_down = cv2.resize(frame, down_points, interpolation= cv2.INTER_LINEAR)

        # Make detections 
        results = model.model(resized_down)
        print(results)
        temp_emotion = ''
        temp_state = ''
        #print(results.pred[0][0])
        if len(results.pred[0]) > 0:
        
            emotion.append(results.pred[0][0][4].item())
            temp_emotion = results.pred[0][0][4].item()
            state.append(results.names[int(results.pred[0][0][5].item())])
            temp_state = results.names[int(results.pred[0][0][5].item())]
        else:
            emotion.append(0)
            temp_emotion = 0
            state.append('none')
            temp_state = 'none'

        cv2.imshow('YOLO', np.squeeze(results.render()))
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        if current_frame >= total_frames:
            cap.release()
            #torch.cuda.empty_cache()
            cv2.destroyAllWindows()
        out = {
            temp_state: temp_emotion * 100,
            "total_frames": total_frames,
            "current_frame": current_frame,
            "total_time": time,
            "time": current_time,
            "fps": frame_rate
        }
        #yield json.dumps(out) + "|"
    #self.close()
    return
    print(emotion)
    print(state)

##def clear_cache():
##        import os
##        import shutil
##        print("Cleared")
##        usr_folder = os.environ['USERPROFILE']
##        directory_path = os.path.join(usr_folder,'.cache', 'torch')
##        shutil.rmtree(directory_path)
        
            
        
        

##    cap.release()
##    cv2.destroyAllWindows()
    #return [emotion, state]
    #'C:/Users/PAVILION/AppData/Local/Programs/Python/Python37/Fucking_first/Fucking_first_app/upload/HG_AIM.mp4'
detection('C:/Users/PAVILION/AppData/Local/Programs/Python/Python37/Drowsiness_detect/yolov5/data/images/zidane.jpg', location)
##detection('C:/Users/PAVILION/AppData/Local/Programs/Python/Python37/Fucking_first(2)/Fucking_first/Fucking_first_app/upload/sample.mp4', location) 


