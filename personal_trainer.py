import time 
import mediapipe as mp
import cv2
import numpy as np
from pose_estimation import PoseDetector
import math



def calculate_angle(a,b,c):
    #b is the origin 
    #ba 
    #bc are the 2 lines 

    # Vector BA
    ba_x = a[0] - b[0]
    ba_y = a[1] - b[1]

    #Vector BC
    bc_x=c[0]-b[0]
    bc_y=c[1]-b[1]


    dot_prod = ba_x * bc_x + ba_y * bc_y

    magnitude_ba=math.sqrt((ba_x)**2+(ba_y)**2)
    magnitude_bc=math.sqrt((bc_x)**2+(bc_y)**2)

    cos_angle = dot_prod / (magnitude_ba * magnitude_bc)
    cos_angle = max(-1, min(cos_angle, 1))


    # Calculate angle in radians
    angle_rad = math.acos(cos_angle)

    # Convert to degrees
    angle_deg = math.degrees(angle_rad)

    return angle_deg




cap= cv2.VideoCapture(0)
pTime =0
detector=PoseDetector()

rep_counter=0


#initial conditions
state_left="down"

state_right="down"

while True:
    success,img=cap.read()
    img=cv2.flip(img,1)
    h,w=img.shape[:2]
    detector.findPose(img)

    lmList=detector.findLandmark(img)


    if len(lmList)!=0:

        #struggle with 15,16=>wrist
        #struggle with 13,14=>elbow
        #struggle with 11,12=>sholuder
        #i want the angle between lines (15,13) and lines(13,11)
        p_16=[lmList[15][1],lmList[15][2]]
        p_14=[lmList[13][1],lmList[13][2]]
        p_12=[lmList[11][1],lmList[11][2]]

        p_15=[lmList[16][1],lmList[16][2]]
        p_13=[lmList[14][1],lmList[14][2]]
        p_11=[lmList[12][1],lmList[12][2]]

        
        angle_left=calculate_angle(p_15,p_13,p_11)
        angle_right=calculate_angle(p_16,p_14,p_12)

        # Update state and count reps
        if angle_right <40 and state_right == "down":
            state_right = "up"
        elif angle_right > 160 and state_right == "up":
            state_right = "down"
        elif angle_left <40 and state_left=="down":
            state_left="up"
        elif angle_left> 160 and state_left=="up":
            rep_counter = rep_counter+1
            state_left="down"

        cv2.circle(img,(lmList[13][1],lmList[13][2]),3,(255,0,255),1)
        cv2.circle(img,(lmList[14][1],lmList[14][2]),3,(255,0,255),1)
        
        cv2.putText(img,str(int(angle_left)),(lmList[14][1]+20,lmList[14][2]),4,2,(255,0,255),2)
        cv2.putText(img,str(int(angle_right)),(lmList[13][1]-20,lmList[13][2]),4,2,(255,0,255),2)        
        
        # Display rep count and current state
        cv2.putText(img, f"Reps: {rep_counter}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        
        cv2.putText(img,f"State_right: {state_right}",(50, 150),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)  
        cv2.putText(img,f"State_left: {state_left}",(50,200),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)

    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img,str(int(fps)),(70,50),1,1,(255,0,255),1)
    cv2.imshow("Image", img)
    cv2.waitKey(1)