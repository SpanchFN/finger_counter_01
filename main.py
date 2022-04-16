import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mp_Hands = mp.solutions.hands
hands = mp_Hands.Hands(max_num_hands = 2)
mpDraw = mp.solutions.drawing_utils  

fingers_coord = [(8, 6),(12, 10),(16, 14),(20, 18)]
thumb_coord = (4, 2)

while cap.isOpened():
    success, image = cap.read()
    image = cv2.flip(image, 1)
    if not success:
        print("Не удалось получить кадр с web-камеры")
        continue

    RGB_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(RGB_image)
    multiLandMarks = results.multi_hand_landmarks 

if multiLandMarks:
    for idx, handLms in enumerate(multiLandMarks):
        or idx.handLms in 

    cv2.imshow("web-cam", image)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()


