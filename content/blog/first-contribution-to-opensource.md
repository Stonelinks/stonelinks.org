#My First Contribution to Open Source Software!
3/27/2012

I'll preface this whole thing with a huge plug for an awesome program called OpenTLD. Its a program for tracking objects (not just faces) in unconstrained video streams with NO training data beforehand. Instead of using precomputed classifiers (like I previously did with OpenCV), OpenTLD builds a model of what it is supposed to be detecting on the fly based on user selection at the start of the program. To demonstrate, here is a slightly creepy demo of OpenTLD tracking my face:

<center><iframe width="420" height="315" src="http://www.youtube.com/embed/gLsdHmCKoEw" frameborder="0" allowfullscreen></iframe></center>

The version of OpenTLD is actually the C++ implementation of a bunch of [Matlab programs](https://github.com/zk00006/OpenTLD) written as part of Zdenek Kalal's PHD thesis. [Here](http://www.youtube.com/watch?v=1GhNXHCQGsM) is a more advanced video by him talking / showing off OpenTLD (what he calls Predator).

But so yeah! [I actually contributed to this](https://github.com/gnebehay/OpenTLD/pull/11)! Even though the code I contributed is trivial (it had to do with the bounding box when you first start the program), it still makes me really excited. Up until now all my contributions to open source have been programs I have written. So it feels really cool to have a change I made rolled into this super advanced computer vision program.

