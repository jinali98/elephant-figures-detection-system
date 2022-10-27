import cv2 as cv
import numpy as np
# from ..data.server import *
from datetime import datetime

cap = cv.VideoCapture('resources/elephant4.mp4')
cap.set(3, 240);
cap.set(4, 380);

classNames = []
classFile = 'coco.names';
# importing all the class names from the coco.names file
with open(classFile, 'r') as f:
    classNames = f.read().rstrip('\n').split('\n')

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightPath = 'frozen_inference_graph.pb'

net = cv.dnn_DetectionModel(weightPath, configPath)
net.setInputSize(320,320);
net.setInputScale(1.0/127.5);
net.setInputMean((127.5, 127.5, 127.5));
net.setInputSwapRB(True);

isElephant = False;

while (cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
    classids, confs, bboxes = net.detect(frame, confThreshold = 0.5)
    if len(classids) != 0:
        for classid, conf, box in zip(classids.flatten(), confs.flatten(), bboxes):
            #  add rectangle only if the classid is 22 (elephant) or 1 (person)
            if classid == 1:
                cv.rectangle(frame, box, color=(255,0,0), thickness=2)
                cv.putText(frame, classNames[classid-1], (box[0] + 10, box[1]+20), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                current_date = now.strftime("%d/%m/%Y")
                # mydict = { "date": current_date, "time": current_time }
                # mycol.insert_one(mydict)


            elif classid == 22:
                cv.rectangle(frame, box, color=(0,255,0), thickness=2)
                cv.putText(frame, classNames[classid-1], (box[0] + 10, box[1]+20), cv.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                current_date = now.strftime("%d/%m/%Y")
                # mydict = { "date": current_date, "time": current_time }
                # mycol.insert_one(mydict)

    # print(classids, confs, bboxes)

    cv.imshow('Original', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
     break