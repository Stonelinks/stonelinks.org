#Universal "Apps" IDE

<hr>

<b>Guest at 2010-03-22 05:31:14:</b><br /><br />

With the rise of Netbooks, migrating more and more processing and storage to "the Cloud," and the popularization of the Adobe AIR and Mozilla Prism platforms that bring web applications to the desktop, we are drifting away from traditional, all-inclusive programs and starting to use smaller and more specialized "apps". 

Can we develop a "universal" app IDE with porting to mobile (iPhone/Windows Phone/Google Phone), web, and more traditional (notebook/desktop/netbook) platforms?

Or is the Internet + AIR/Prism already doing that?

See Intel's new AppUp store
http://www.intel.com/Consumer/Products/appup.htm

<hr>

<b>Guest at 2010-03-22 06:09:39:</b><br /><br />

Oh man so hard yes. This is the kind of thing I wish ANSI or IEEE or something thought of before six companies came out with mobile phone OSes.

Side notes:

- I just tried out an Adobe AIR application and it performed like an abortion in the back of a Nascar during the Daytona 500
- Mozilla prism seems like a web browser without navigation controls plus a few basic features. Not at all a bad idea.
- I like how Windows vista is not supported in Appup but XP is

The way I see getting this done, at least for phones, is writing several separate platform specific applications (one for windows phone, android, iphone, webOS, blackberry, etc) that function as an abstraction layer. This, while potentially cantankerous, monstrously inefficient, limited or all of the above, would be designed to provide the would-be application programmer a standard instruction set available across all platforms. One could then do the same thing but on a computer and bingo, the app is running on something other than a phone.

Of course you make a very strong point that the web browser is basically the universal application nowadays, which might render the previous paragraph useless
