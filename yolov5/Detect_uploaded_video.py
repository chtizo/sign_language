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
   

    
    
    model = torch.hub.load('ultralytics/yolov5', 'custom', path= location + 'runs/train/exp28/weights/last.pt', force_reload=True)
    model.conf = 0.25
    model.iou = 0.45
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
        results = model(frame)
        #print(vars(results))
        print(results.pred[0])
        
##        awake = 0
##        drowsy = 0
##        happy = 0
##        stressed = 0
##
##        #print(results.pred)
##        
##        i = len(results.pred[0]) - 1
##        while i >= 0:
##            if results.pred[0][i][-1].item() == 15:
##                awake = results.pred[0][i][-2].item()
##            if results.pred[0][i][-1].item() == 16:
##                drowsy = results.pred[0][i][-2].item()
##            if results.pred[0][i][-1].item() == 17:
##                happy = results.pred[0][i][-2].item()
##            if results.pred[0][i][-1].item() == 18:
##                stressed = results.pred[0][i][-2].item()
##            i -= 1

        cv2.imshow('YOLO', np.squeeze(results.render()))
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
##        if current_frame >= total_frames:
##            cap.release()
##            #torch.cuda.empty_cache()
##            #cv2.destroyAllWindows()
##        out = {
##            "awake": awake * 100,
##            "drowsy": drowsy * 100,
##            "happy": happy * 100,
##            "stressed": stressed * 100,
##            "total_frames": total_frames,
##            "current_frame": current_frame,
##            "total_time": time,
##            "time": current_time,
##            "fps": frame_rate
##        }
##        yield json.dumps(out) + "|"
    #self.close()
    return 
    #print(emotion)
    #print(state)

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
detection("Sample_all.mp4", location)
#detection('C:/Users/PAVILION/AppData/Local/Programs/Python/Python37/Fucking_first(2)/Fucking_first/Fucking_first_app/upload/Sample_all.mp4', location) 


