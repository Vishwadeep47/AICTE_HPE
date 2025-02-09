import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

video_source = 0
cap = cv2.VideoCapture(video_source)
#cap = cv2.VideoCapture("run.mov")

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

with mp_pose.Pose(static_image_mode=False, model_complexity=0, enable_segmentation=False) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Video capture ended")
            break

        frame = cv2.flip(frame, 1)

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = pose.process(frame_rgb)

        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2)
            )

        display_frame = cv2.resize(frame, (960, 540))

        cv2.imshow('Pose Estimation', display_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
