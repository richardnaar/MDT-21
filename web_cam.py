import cv2
from psychopy import core
import os  # handy system and path functions

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)  # set as a current dir

clock = core.Clock()

vid_capture = cv2.VideoCapture(0)

vid_cod = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter(
    _thisDir+"\\videos\\cam_video.mp4v", vid_cod, 20.0, (640, 480))


t = clock.getTime()
while(clock.getTime()-t < 6):
    # Capture each frame of webcam video
    ret, frame = vid_capture.read()
    cv2.imshow("My cam video", frame)
    output.write(frame)
    # Close and break the loop after pressing "x" key
    if cv2.waitKey(1) & 0XFF == ord('x'):
        break

# close the already opened camera
vid_capture.release()
# close the already opened file
output.release()
# close the window and de-allocate any associated memory usage
cv2.destroyAllWindows()
