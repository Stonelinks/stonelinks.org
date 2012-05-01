#Active Face Tracking with Stonebot
03/14/2011

I finally have it working! Very excited as I write this. So glad spring break exists otherwise I'd never have the time for this. Long story short, I have face detection working on my personal robot, watch the video to see it in action.

<center>
<iframe width="80%" height="400px" src="http://www.youtube.com/embed/RRwMJ8GYT7Y" frameborder="0" allowfullscreen></iframe>
</center>

This has been a goal of mine ever since I started building my personal robot (which, in keeping with the Stonelinks legacy, shall henceforth be known as "Stonebot"). This face tracking makes use of my [new method for positioning the camera](a-more-accurate-coordinate-system.html) that I worked on a little over winter break, and is definitely the most complicated piece of python I have written to date. Here are some highlights of the project:

##The Hardest Part: OpenCV

By far, the hardest thing about this was getting OpenCV set up correctly. Once set up, it is relatively easy to use, comes with a lot of cool examples and seems extremely powerful (if you don't believe me check out what the folks over at [Willow Garage](http://www.willowgarage.com/) do with it on a routine basis). In the future it is definitely something I want to experiment more with, and not just use for face and object detection.

So to set it up: If you're like me and running Ubuntu 10.04, you'll want to save some time from having to compile OpenCV from source (especially if you are on a 900MHz single core eee like I originally was). Unfortunately, the most recent version of OpenCV is 2.2 while the latest version in the official Ubuntu repos it is only 2.0. Now normally I would not care about using an older version of the same library, however when I looked at the python examples for 2.2, 2.1 and 2.0, things looked much cleaner in 2.2 and 2.1 (you can import everything using `import cv` in 2.1 on up).

Additionally, presumably the newer something is, the better it will be. I tried compiling OpenCV 2.1 and 2.2 a couple of times with no luck on various machines (the eee included... that took about an hour and a half). However I was delighted to find that someone that someone had compiled 2.1 for Ubuntu 10.04 and 10.10. All that was needed to be done to install it was:

<pre>
$ sudo add-apt-repository ppa:gijzelaar/OpenCV2
$ sudo apt-get update
$ sudo apt-get install OpenCV python-OpenCV
</pre>

and OpenCV is yours for the taking! Install the documentation and run the examples to figure out if all your V4L2 and webcam drivers will play nice with it.

##Classifiers are easily fooled

![image](http://i.imgur.com/XPuhpl.jpg)

This is pretty self explanatory. I drew the above face with a purple magic marker in about five seconds and it is able to fool the Haar classifier.

Additionally, I have found that the wrong lighting, glasses, and long hair can throw it off as well. To be fair, Haar feature detection in this case is not incredibly accurate. The advantage it possesses in this application is relatively low computational complexity which translates into a speedy detection algorithm.

##CPU speed

As I said in the video, performance on the eee PC was terrible. While not surprising, this is kind of upsetting as I was considering putting it to use as the brains of the robot once I add some sort of locomotion to the system. I was pleasantly surprised however when I loaded up the code on to my new laptop (which has a Core 2 duo operating at 1.3GHz) and things worked beautifully. It would seem that OpenCV, even though I thought that python couldn't be threaded, is somehow threading itself across both cores of the processor. As I'm still nrew to python, I'm looking into how this works. 
