#LabVIEW Custom Documentation Formats

LabVIEW is a necessary evil, but sometimes it pulls through. Earlier today I found myself in the position of needing a whole bunch of icons, block diagrams and VI hierarchies extracted from a bunch of LabVIEW that I wrote for work to go in my documentation, which is in written in LaTeX.

Up until now I thought this would mean trying to do a million screenshots over VNC on my work computer, and then going back and cropping what I needed. However on further research I was thrilled to find out that LabVIEW can pretty much do this on its own. See the <a href="http://zone.ni.com/reference/en-XX/help/371361B-01/lvconcepts/printing_vis/">NI website on printing VI documentation</a>.

Basically what I did was import the VI hierarchy for my top level VI (the dashboard in this case), created a custom format for my documentation, checked off what I wanted to appear, and then outputted it all as HTML. The end result looks <a style="font-size: 13.2px;" href="http://stonelinks.org/luke/work/cfa/example/">something like this</a>. Since the directory where the HTML was generated is now chock full o' images, I took what images I wanted and insert them into my documentation. Probably an hour of tedious work saved!

Just goes to show you how a user can find many different ways to use a one part of a program for what it might not have originally been intended.
