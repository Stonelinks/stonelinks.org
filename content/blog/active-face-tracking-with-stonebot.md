#Active face tracking with Stonebot

I finally have it working! Very excited as I write this. So glad spring break exists otherwise I'd never have the time to do stuff like this. Long story short, I have face detection working on my personal robot, watch the video and check out the code below to see it in action.
<center><iframe title="YouTube video player" width="480" height="390" src="http://www.youtube.com/embed/RRwMJ8GYT7Y" frameborder="0" allowfullscreen></iframe></center>
This has been a goal of mine ever since I started building my personal robot (which, in keeping with the Stonelinks legacy, shall henceforth be known as "Stonebot"). This face tracking makes use of my <a href="http://stonelinks.org/2011/01/07/a-more-accurate-coordinate-system/">new method for positioning the camera</a> that I worked on a little over winter break, and is definitely the most complicated piece of python I have written to date.

I've posted the code below, which I have tediously commented and explained things in detail for anyone who reads through it. However, some things are not so obvious from the code or maybe you don't want to read it. Whatever the case, here are the highlights of the project<!--more-->:

<strong>The Hardest Part: openCV</strong>

By far, the hardest thing about this was getting openCV set up correctly. Once set up, it is relatively easy to use, comes with a lot of cool examples and seems extremely powerful (if you don't believe me check out what the folks over at willow garage do with it on a routine basis). In the future it is definitely something I want to experiment more with, and not just use for face and object detection.

So to set it up: If you're like me and running Ubuntu 10.04, you'll want to save some time from having to compile openCV from source (especially if you are on a 900MHz single core eee like I originally was). Unfortunately, the most recent version of openCV is 2.2 while the latest version in the official Ubuntu repos it is only 2.0. Now normally I would not care about using an older version of the same library, however when I looked at the python examples for 2.2, 2.1 and 2.0, things looked much cleaner in 2.2 and 2.1 (you can literally import everything using <code>import cv</code> in 2.1 on up). Additionally, presumably the newer something is, the better it will be.

I tried compiling openCV 2.1 and 2.2 a couple of times with no luck on various machines (the eee included... that took about an hour and a half). However I was delighted to find that someone that someone had compiled 2.1 for Ubuntu 10.04 and 10.10. All that was needed to be done to install it was:
<code>
  $ sudo add-apt-repository ppa:gijzelaar/opencv2
  $ sudo apt-get update
  $ sudo apt-get install opencv python-opencv
</code> 
and openCV is yours for the taking! Install the documentation and run the examples to figure out if all your V4L2 and webcam drivers will play nice with it.

<strong>Classifiers are easily fooled</strong>


<img src="http://i.imgur.com/XPuhpl.jpg" alt="" title="" />

This is pretty self explanatory. I drew the above face with a purple magic marker in about five seconds and it is able to fool the Haar classifier. Additionally, I have found that the wrong lighting, glasses, and long hair can throw it off as well. To be fair, Haar feature detection in this case is not incredibly accurate. The advantage it possesses in this application is relatively low computational complexity which translates into a speedy detection algorithm.


<strong>CPU speed</strong>

As I said in the video, performance on the eee PC was terrible. While not surprising, this is kind of upsetting as I was considering putting it to use as the brains of the robot once I add some sort of locomotion to the system.

I was pleasantly surprised however when I loaded up the code on to my new laptop (which has a core 2 duo operating at 1.3GHz) and things worked beautifully. It would seem that openCV, even though I thought that python couldn't be threaded, is somehow threading itself across both cores of the processor.


<strong>Code</strong>
<pre class="brush:python">
#!/usr/bin/python
"""
    File: facetracker.py
    Author: Lucas Doyle - stonelinks.org
    Last edited: 3/14/11
    Purpose:
        This program uses openCV to do object detection using haar-cascade classifiers.
        Specifically, this program looks for faces in a webcam's feild of view
        Upon detecting a face, the program moves the pan / tilt module to center the face
        on the screen. When a face is not detected for awhile, the pan / tilt
        moves back and fourth in an attempt to search for one

    GPL, no warranty express or implied, etc

    Based on facedetect.py in the OpenCV 2.1 samples
"""

from optparse import OptionParser
import cv
import time
import sys
import serial

"""
    Parameters for haar detection
    From the API:
    The default parameters (scale_factor=2, min_neighbors=3, flags=0) are tuned
    for accurate yet slow object detection. For a faster operation on real video
    images the settings are:
    scale_factor=1.2, min_neighbors=2, flags=CV_HAAR_DO_CANNY_PRUNING,
    min_size is less than or equal to minimum possible face size
"""

min_size = (20, 20)
image_scale = 2
haar_scale = 1.3
min_neighbors = 2
haar_flags = 0
search_scale = 5 # scale for search mode. higher means search faster.

window_name = "Face Tracking"
usbport = '/dev/ttyUSB0'

def move(servo, angle):
    """
        moves servo at index 'servo' to angle 'angle'
        current pin assignments:
            1 --> x axis of pantilt
            2 --> y axis of pantilt
    """
    
    # start servo transmission (255) on the correct servo
    ser.write(chr(255))
    ser.write(chr(servo))
    
    # hardware corrections for pan tilt module
    # shift angle according according to measured centers from servoutils
    if (servo == 1) : middle = 99
    if (servo == 2) : middle = 118
    angle = angle + middle - 90
    
    # truncate angle to something realistic if outside bounds
    if (angle < 0) : angle = 0
    if (angle > 180) : angle = 180
    
    # write the angle to the serial port
    ser.write(chr(angle))

def detect_and_draw(img, cascade):
    """
        This function is based heavily on the one with the same name
        in facedetect.py in the openCV samples. It detects and draws a
        rectangle around a single object in the image based on the cascade
        given to it. Returns the center coordinates of this rectangle
    """

    grey = cv.CreateImage((img.width,img.height), 8, 1)
    small_img = cv.CreateImage((cv.Round(img.width / image_scale), cv.Round (img.height / image_scale)), 8, 1)
 
    # convert color input image to greyscale
    cv.CvtColor(img, grey, cv.CV_BGR2GRAY) # damn British spelling
 
    # scale input image for faster processing
    cv.Resize(grey, small_img, cv.CV_INTER_LINEAR)
 
    cv.EqualizeHist(small_img, small_img)
 
    center = None
 
    if(cascade):
        # HaarDetectObjects takes ~0.02s
        faces = cv.HaarDetectObjects(small_img, cascade, cv.CreateMemStorage(0), haar_scale, min_neighbors, haar_flags, min_size)
        if faces:
            # HaarDetectObjects returns a list of tuples, with each element in the list
            # cooresponding to an object that was detected. Since only one face is being tracked,
            # only look at the first element in faces
            ((x, y, w, h), n) = faces[0]
            # the input to cv.HaarDetectObjects was resized, so scale the
            # bounding box of each face and convert it to two CvPoints
            pt1 = (int(x * image_scale), int(y * image_scale))
            pt2 = (int((x + w) * image_scale), int((y + h) * image_scale))
            cv.Rectangle(img, pt1, pt2, cv.RGB(255, 0, 0), 3, 8, 0)
            # get the xy corner co-ords, calc the center location
            x1 = pt1[0]
            x2 = pt2[0]
            y1 = pt1[1]
            y2 = pt2[1]
            centerx = x1 + ((x2-x1)/2)
            centery = y1 + ((y2-y1)/2)
            center = (centerx, centery)
    cv.ShowImage(window_name, img)
    return center
 
def delta(loc, span, max_delta, center_tolerance):
    """
        Compute the change in position to center the webcam.
        loc is the face's center for this axis
        span is the width/height of the axis
        max_delta is the max number of degrees to move
        center_tolerance is the center region where we don't allow movement
    """
    framecenter = span/2
    delta = framecenter - loc
    if abs(delta) < center_tolerance:
        delta = 0 # don't move, this prevents oscillations
    else:
        is_neg = delta <= 0
        
        # basically, make delta smaller the closer we are to the center
        to_get_near_center = abs(delta) - center_tolerance
        if to_get_near_center > 45:
            delta = 4
        elif to_get_near_center > 35:
            delta = 3
        elif to_get_near_center > 25:
            delta = 2
        else:
            # move real slow if we're very near center
            delta = 1
        if is_neg:
            delta = delta * -1
    return delta
 
if __name__ == '__main__':

    # open up serial port and connect to Arduino
    # Note: mine is set at a really high baud so I can
    # make my servos move short increments very fast
    ser = serial.Serial(usbport, 115200, timeout=10)
    
    # center servos
    x = y = 90
    move(1, x)
    move(2, y)
    
    # parse cmd line options, setup Haar classifier (much of this taken from openCV facedetect.py)
    parser = OptionParser(usage = "usage: %prog [options] [camera_index]")
    parser.add_option("-c", "--cascade", action="store", dest="cascade", type="str", help="Haar cascade file, default %default", default = "haarcascade_frontalface_alt.xml")
    (options, args) = parser.parse_args()
 
    cascade = cv.Load(options.cascade)
 
    if len(args) != 1:
        parser.print_help()
        sys.exit(1)
 
    input_name = args[0]
    if input_name.isdigit():
        capture = cv.CreateCameraCapture(int(input_name))
    else:
        print "We need a camera input! Specify camera index e.g. 0 for /dev/video0"
        sys.exit(0)
 
    cv.NamedWindow(window_name, 1)
 
    if capture:
        frame_copy = None
        frames_with_no_faces = 0
        timestep = 0
        
        # do this forever
        while True:
            frame = cv.QueryFrame(capture)
            if not frame:
                cv.WaitKey(0)
                break
            if not frame_copy:
                frame_copy = cv.CreateImage((frame.width,frame.height), cv.IPL_DEPTH_8U, frame.nChannels)
            if frame.origin == cv.IPL_ORIGIN_TL:
                cv.Copy(frame, frame_copy)
            else:
                cv.Flip(frame, frame_copy, 0)
            
            # do face detection
            center = detect_and_draw(frame_copy, cascade)
            
            if center != None:
                # a face was found!
                cx = center[0]
                cy = center[1]
                
                # reset this variable
                frames_with_no_faces = 0

                # find out what delta should be
                xdelta = delta(cx, frame_copy.width, 6, 15) * -1
                ydelta = delta(cy, frame_copy.height, 1, 25) * -1
 
                delta_mag = abs(xdelta)+abs(ydelta)
                if delta_mag > 0:
                    x = x + xdelta
                    y = y + ydelta
                    
                    # actually move the servos
                    move(1, x)
                    move(2, y)
                    
                    # sleep for a little bit to dampen oscillations
                    time.sleep(.05)
                    
                    # clear center
                    center = None
            else:
                # increment time step
                timestep += 1

                
                # increment no_faces count
                frames_with_no_faces+=1
                
                # no faces for roughly 6 seconds
                if frames_with_no_faces > 30:
                    # search for faces!
                    
                    # move the x axis back and forth with each timestep 
                    if timestep < (180 / search_scale):
                        x = search_scale * (timestep % (180 / search_scale))
                    elif (timestep >= (180 / search_scale)) and (timestep < (2 * 180 / search_scale)):
                        x = 180 - (search_scale * (timestep % (180 / search_scale)))
                    else:
                        timestep = 0
                    move(1, x)
                    
                    # center the y axis
                    y = 90
                    move(2, y)
            if cv.WaitKey(10) >= 0:
                break
    cv.DestroyWindow(window_name)
</pre>
