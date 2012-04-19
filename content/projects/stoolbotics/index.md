#Stoolbotics

<center>

<br>

<iframe width="420" height="315" src="http://www.youtube.com/embed/h3Rus5mUkzY" frameborder="0" allowfullscreen></iframe>

</center>

Stoolbotics is a general purpose robotic arm and kinematics simulator aimed at being a teaching tool for aspiring roboticists. The motivation for this project was simple: the linear algebra and mathematical concepts behind robotics is difficult for a beginner to understand without any visual context. This is especially true for people who are primarily visual learners.

This tool will hopefully fill a gap in many higher education robotics classrooms. It was designed to be easy to use and compatible with other technologies (like MATLAB). The project itself was conceived and implemented halfway through the Fall 2011 semester at RPI by Lucas Doyle with some help from Scott Peck.

##Features

Stoolbotics has many features that make it attractive to the aspiring roboticst and the higer education robotics classrom. To name a few, Stoolbotics features:

- Low barrier to entry eith an easy to use file format for specifying a robot arm
- Ability to visualize any robot that can be specified in such a file
- Compute the forward kinematics of any robot
- Animate and draw paths for arms
- Command line interface within simulator with many useful commands
- Completely customizable simulation environment (time-stepping, etc)
- Ability to record simulator activity
- Ability to playback saved recordings, or even import a recording generated in MATLAB
- Able to be driven in real time from a UDP stream from other programs like MATLAB (includes an example)
- Change variables in the simulator on the fly
- Built in help from simulator command line, and of course this stellar and complete documentation
- Cross platform implementation

##Getting Stoolbotics
###For Windows
####Prebuilt (recommended)

Stoolbotics comes in a pre-packaged, portable build for Windows. You can download it from Lucas' Dropbox here: [http://dl.dropbox.com/u/4428042/simulator.zip](http://dl.dropbox.com/u/4428042/simulator.zip).

Simply unzip and run <code>stoolbotics.bat</code>, and you should be up and running!

####From Source
If you're feeling more adventurous, or want to develop Stoolbotics for Windows, you can still run the simulator through python from the command prompt. You will need to install a few dependencies though. Python (2.7 works best), Numpy, PyOpenGL and (optionally) the python imaging library (PIL) need to all be installed. If you choose not to install PIL, the only functionality that will be effected is the ability to take screenshots from within the simulator.

Once you have everything above installed, you should [download the latest zip](https://github.com/Stonelinks/Stoolbotics/zipball/master) of our code repository from github. Once you have it downloaded, just unzip and run <code>python simulator.py</code> in the simulator directory.

###For Linux

Make sure you have Python, Git, Numpy, PyOpenGL and (optionally) the python imaging library (PIL) installed. Using pip, python's distutils, or your Linux distributions package manager is appropriate here. If you choose not to install PIL, the only functionality that will be affected is the ability to take screenshots from within the simulator.

Next, make a clone of our repository by running <code>git clone https://github.com/Stonelinks/Stoolbotics.git</code>, then just run <code>sh Stoolbotics.sh</code> to fire up the simulator. Any time you wish to update, just run <code>git pull</code> from inside the repository.

###For Mac OSX

OSX isn't officially supported as we don't have a machine we can test on, but if you have a python installation with PyOpenGL, Numpy, and PIL then there is no reason why following the Linux instructions above wouldn't work.

If you just want to grab a copy of the code, you can [download the latest zip](https://github.com/Stonelinks/Stoolbotics/zipball/master) of our code repository from github.





