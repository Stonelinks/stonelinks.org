#First Contribution to someone else's Open Source Software
3/27/2012

<center><iframe width="500px" height="400px" src="http://www.youtube.com/embed/gLsdHmCKoEw" frameborder="0" allowfullscreen></iframe></center>

Up until now, all my contributions to open source have been programs I have written, and as a general practice I like to make all my work open source if I can. However, its a nice and refreshing feeling to have some code I wrote incorporated into someone else's project for a change.

The program in question here is called [OpenTLD](https://github.com/gnebehay/OpenTLD). Its a program for tracking objects (not just faces) in unconstrained video streams with NO training data beforehand (TLD stands for Tracking, Learning and Detection). Instead of using precomputed classifiers (like I previously have done with OpenCV), OpenTLD builds a model of what it is supposed to be detecting on the fly. To demonstrate, above is a slightly creepy demo of OpenTLD tracking my face.

The version of OpenTLD here is actually the C++ implementation of OpenTLD. OpenTLD began life as a bunch of [Matlab programs](https://github.com/zk00006/OpenTLD) written as part of Zdenek Kalal's PHD thesis. [Here](http://www.youtube.com/watch?v=1GhNXHCQGsM) is a more advanced video by him talking / showing off OpenTLD (he calls it Predator).

But so yeah! [I actually contributed to this](https://github.com/gnebehay/OpenTLD/pull/11)! Even though the code I wrote is trivial (it had to do with the bounding box when you first start the program), it still makes me really excited. I plan on taking a closer look at the codebase sometime later and trying to learn how it works. Up until now all my contributions to open source have been programs I have written. It feels really cool to have a change I made rolled into this super advanced computer vision program!
