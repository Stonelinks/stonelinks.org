#Ice Thickness Robot

<hr>

<b>Guest at 2010-03-22 04:41:07:</b><br /><br />

Every year people and machines fall through the ice on ponds and lakes. The side effects misjudgment of of ice thickness can be anything from hypothermia, loss of an expensive piece of equipment, or even death.

If a robot were made to autonomously monitor and display the thickness of ice on a body of water, it very well could help avoid these kinds of situations.

The robot would have to be able to withstand the elements and traverse the terrain normally encountered on a frozen body of water. It could use GPS data / google maps to navigate the frozen body of water, gauge ice thickness, and report back to some kind of server if the ice is safe or not.

The key to everything is the bots ability to accurately determine the thickness of the ice. This could be done with ultrasound or with a small drill.

The approach I favor most is the drill due to my immediate ease of understanding. Basically the robot would drill a hole in the ice and lower a probe with exposed contacts on the end. If the probe hits water, the circuit completes and the robot records the depth of the probe. If the depth is less than what a human could stand, then the ice is not safe.<hr>

<b>Guest at 2010-03-22 05:12:54:</b><br /><br />

My immediate concerns would be the cost of replacing a robot like this, should the worst happen and it fall through the ice. Is there any way to do this remotely using radio waves, sonar, etc. (If this sounds foolish, my knowledge of sonic properties is sorely lacking.) <hr>

<b>Guest at 2010-03-22 05:41:37:</b><br /><br />

This is not at all a foolish concern. Inevitably, as with all design problems, it must be assumed that the end user will do absolutely everything wrong when using your product. The bot falling through the ice would be an expensive mistake indeed.

The best way to fix a problem like this is to prevent it. The way to do this would be to minimize the weight of the robot while maximizing the effective surface area of the drive components in contact with the ground. Something like treads are ideally suited for applications like this. Making the machine float / waterproof is another, more complicated option.

As for your suggestion, I am by no means an expert either, but I do know that ultrasonics are used primarily for seeing changes in density, and therefore edges, in objects. Sonar is like ultrasound, only it is more accurate over long ranges and only works in a single medium.

In short, I don't know what the ideal wave-based solution would be.
