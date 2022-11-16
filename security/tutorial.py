import cv2
import time
import datetime

cap = cv2.VideoCapture(0)  # capture. 0 means you have 1 camera.

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

body_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_fullbody.xml")

detection = False
detection_stopped_time = None
timer_started = False
SECONDS_TO_RECORD_AFTER_DETECTION = 5

frame_size = (int(cap.get(3)), int(cap.get(4)))
# * means you'll seperate the parameter to each characters. => ("m", "p", "4", "v")
fourcc = cv2.VideoWriter_fourcc(*"mp4v")


while True:
    _, frame = cap.read()  # _ is a placeholder. Capture the frame

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect our faces and bodies in the frame, in the grayscale
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    bodies = face_cascade.detectMultiScale(gray, 1.3, 5)
    # (graysccale image, scale factor: the number determines the accuracy and speed of this algorithm - 1.1:accurate to 1.5:fast, minimum number of neighbor: the higher the number goes, the less number of faces you're gonna get detected)

    if len(faces) + len(bodies) > 0:  # have we detected or seen any face or body?
        if detection:
            timer_started = False  # if we were about to end the video
        else:
            detection = True  # if we were not recording before, start recording
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            out = cv2.VideoWriter(
                f"{current_time}.mp4", fourcc, 20, frame_size)
            print("Started recording!")
    elif detection:  # if we were not detecting faces or bodies and we're recording, then it's time to start the timer
        if timer_started:
            if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                detection = False
                timer_started = False
                out.release()
                print('Stop Recording!')
        else:  # if the timer not started, we start the timer and keep track of when we start at the time
            timer_started = True
            detection_stopped_time = time.time()

    if detection:
        out.write(frame)

    # for (x, y, width, height) in faces:
    #     cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)
    #     # rectangle(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)

    cv2.imshow("Camera", frame)  # displaying the frame on the screen

    if cv2.waitKey(1) == ord('q'):
        break

out.release()
cap.release()
cv2.destroyAllWindows()

# if you found 'ImportError: No module named cv2', put this command in your terminal. pip install opencv-python
# when you start python tutorial.py, you will see a poped-up camera screen. if you want to quit the camera, press Q button.
