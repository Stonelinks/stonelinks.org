#Download

<br>

##For Windows

<br>

####Prebuilt (recommended)

Stoolbotics comes in a pre-packaged, portable build for Windows. You can download it from Lucas' Dropbox here: [http://dl.dropbox.com/u/4428042/simulator.zip](http://dl.dropbox.com/u/4428042/simulator.zip).

Simply unzip and run <code>stoolbotics.bat</code>, and you should be up and running!

<br>

####From Source

If you're feeling more adventurous, or want to develop Stoolbotics for Windows, you can still run the simulator through python from the command prompt. You will need to install a few dependencies though. Python (2.7 works best), Numpy, PyOpenGL and (optionally) the python imaging library (PIL) need to all be installed. If you choose not to install PIL, the only functionality that will be effected is the ability to take screenshots from within the simulator.

Once you have everything above installed, you should [download the latest zip](https://github.com/Stonelinks/Stoolbotics/zipball/master) of our code repository from github. Once you have it downloaded, just unzip and run <code>python simulator.py</code> in the simulator directory.

<br>

##For Linux

Make sure you have Python, Git, Numpy, PyOpenGL and (optionally) the python imaging library (PIL) installed. Using pip, python's distutils, or your Linux distributions package manager is appropriate here. If you choose not to install PIL, the only functionality that will be affected is the ability to take screenshots from within the simulator.

Next, make a clone of our repository by running <code>git clone https://github.com/Stonelinks/Stoolbotics.git</code>, then just run <code>sh Stoolbotics.sh</code> to fire up the simulator. Any time you wish to update, just run <code>git pull</code> from inside the repository.

<br>

##For Mac OSX

OSX isn't officially supported as we don't have a machine we can test on, but if you have a python installation with PyOpenGL, Numpy, and PIL then there is no reason why following the Linux instructions above wouldn't work.

If you just want to grab a copy of the code, you can [download the latest zip](https://github.com/Stonelinks/Stoolbotics/zipball/master) of our code repository from github.

<br>

##Source Code

Stoolbotics is open source! See the code that runs Stoolbotics on github!
####[https://github.com/Stonelinks/Stoolbotics](https://github.com/Stonelinks/Stoolbotics)

<br>

<script type="text/javascript">
$(window).load(function () {
  var c = new libgithub.Badge('Stonelinks', 'Stoolbotics');
  c.numCommitsIs(5);
  c.targetIs('#commits');
});
</script>

####Latest Commits to Stoolbotics:
<div id="commits"></div>

