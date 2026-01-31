import cv2 
import mediapipe as mp 
import serial  # For Arduino communication 
import time 
 
arduino = serial.Serial('COM3', 9600) 
time.sleep(2) 

mp_drawing = mp.solutions.drawing_utils 
mp_hands = mp.solutions.hands 
mp_face = mp.solutions.face_mesh 

cap = cv2.VideoCapture(0) 
 
with mp_hands.Hands(min_detection_confidence=0.6, min_tracking_confidence=0.6) as hands, mp_face.FaceMesh(min_detection_confidence=0.6, min_tracking_confidence=0.6) as face_mesh: 
 
    while True: 
        success, frame = cap.read() 
        if not success: 
            break 

        frame = cv2.flip(frame, 1) 
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
 
        hand_results = hands.process(rgb) 
        face_results = face_mesh.process(rgb)
        
        if hand_results.multi_hand_landmarks: 
            for hand_landmarks in hand_results.multi_hand_landmarks: 
                mp_drawing.draw_landmarks(frame, hand_landmarks, 
mp_hands.HAND_CONNECTIONS)  
                index_tip = hand_landmarks.landmark[8] 
                wrist = hand_landmarks.landmark[0] 
                 
                if index_tip.y < wrist.y:
                    cv2.putText(frame, "HAND UP!", (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, 
(0,255,0), 2) 
                    arduino.write(b'1') 
                else:
                    cv2.putText(frame, "HAND DOWN!", (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, 
(0,255,0), 2)
                    arduino.write(b'0')
        if face_results.multi_face_landmarks: 
            for face_landmarks in face_results.multi_face_landmarks: 
                mp_drawing.draw_landmarks( 
                    frame, 
                    face_landmarks, 
                    mp_face.FACEMESH_CONTOURS, 
                    mp_drawing.DrawingSpec(color=(0,255,255), thickness=1, circle_radius=1) 
                ) 
 
        cv2.imshow('Mediapipe Integration', frame) 
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break 

cap.release()
cv2.destroyAllWindows