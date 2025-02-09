import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

image_path = "run.jpg"
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

results = pose.process(image_rgb)

if results.pose_landmarks:
    print("Pose landmarks detected!")

    for idx , landmark in enumerate(results.pose_landmarks.landmark):
        print(f"Landmark {idx}: (x: {landmark.x} , y: {landmark.y} , z: {landmark.z}")
    for landmark in results.pose_landmarks.landmark:

        h , w , c =image.shape

        cx , cy = int(landmark.x * w), int(landmark.y * h)

        cv2.circle(image, (cx, cy) , 5, (0 , 255, 0) , -1)


        annotated_image = image.copy()
        mp_drawing.draw_landmarks(
            annotated_image, results.pose_landmarks,mp_pose.POSE_CONNECTIONS)


cv2.imshow("Pose Landmarks", image)
cv2.imshow("Pose drawing", annotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

pose.close(0)
