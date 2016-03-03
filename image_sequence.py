from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import time

start_time = time.time()
#initialize the camera and grab a reference to the raw camera capture

with PiCamera() as camera:
        #camera = PiCamera()
        camera.resolution = (640,480)
        rawCapture = PiRGBArray(camera,size=(640,480))
        #allow camera to warmup
        time.sleep(2)

        #grab an image from camera
        camera.capture(rawCapture, format = "bgr")
        image = rawCapture.array

        #display the image on screen and wait for a keypress
        #cv2.imwrite('image_'+str(i)+'.jpg',image)
        #rawCapture.truncate(0)
        camera.capture_sequence(['image%02d.jpg' % i for i in range(50)])

print ("---- %s seconds ---- " % (time.time() - start_time))
