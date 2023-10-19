import cv2
import mediapipe as mp
import time

print("GESTURE BASED HOME CONTROL SYSTEM")

cap = cv2.VideoCapture(0)
mp_Hands = mp.solutions.hands
hands = mp_Hands.Hands()
mpDraw = mp.solutions.drawing_utils
finger_Coord = [(8, 6), (12, 10), (16, 14), (20, 18)]
thumb_Coord = (4,2)

light_on = False
fan_on = False
curr = time.time()

while True:
    success, image = cap.read()
    RGB_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(RGB_image)
    multiLandMarks = results.multi_hand_landmarks

    if multiLandMarks:
        handList = []
        for handLms in multiLandMarks:
            #mpDraw.draw_landmarks(image, handLms, mp_Hands.HAND_CONNECTIONS)
            for idx, lm in enumerate(handLms.landmark):
              h, w, c = image.shape
              cx, cy = int(lm.x * w), int(lm.y * h)
              handList.append((cx, cy))
        '''for point in handList:
            cv2.circle(image, point, 10, (255, 255, 0), cv2.FILLED)'''
        upCount = 0
        for coordinate in finger_Coord:
            if handList[coordinate[0]][1] < handList[coordinate[1]][1]:
                upCount += 1
        if handList[thumb_Coord[0]][0] > handList[thumb_Coord[1]][0]:
            upCount += 1
        #cv2.putText(image, str(upCount), (150,150), cv2.FONT_HERSHEY_PLAIN, 6, (0,255,0), 12)

        if upCount==1:
                cv2.putText(image, str(upCount)+' - Light ON', (10,50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255,0,0), 4)
        if upCount==2:
                cv2.putText(image, str(upCount)+' - Light OFF', (10,50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255,0,0), 4)
        if upCount==3:
                cv2.putText(image, str(upCount)+' - Fan ON', (10,50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255,0,0), 4)
        if upCount==4:
                cv2.putText(image, str(upCount)+' - Fan OFF', (10,50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255,0,0), 4)
        if upCount==5:
                cv2.putText(image, str(upCount)+' - Fan and Light OFF', (10,50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255,0,0), 4)

        if time.time()>=curr+2:
            curr = time.time()
            
            if light_on == False and upCount==1:
                    light_on = not light_on
                    print('Light ON')
            if light_on == True and upCount==2:
                    light_on = not light_on
                    print('Light OFF')
            if fan_on == False and upCount==3:
                    fan_on = not fan_on
                    print('Fan ON')
            if fan_on == True and upCount==4:
                    fan_on = not fan_on
                    print('Fan 0FF')
            
            if (light_on == True or fan_on == True) and upCount==5:
                    fan_on = False
                    light_on = False
                    print('Light and Fan 0FF')

    cv2.imshow("Counting number of fingers", image)
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()