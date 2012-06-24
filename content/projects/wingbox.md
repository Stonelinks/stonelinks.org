#Boeing Robotic Wingbox

<center>
<img src="{{wr}}static/img/wingbox/screenshot.png" class="thumbnail" width="54%">

Simulation window
</center>

<br>
<br>


##Introduction

The wings of a modern commercial aircraft are one of the most sophisticated, complex and precisely manufactured feats of engineering that mankind has ever produced. Wings not only provide the lift and structural support that allow the aircraft to fly, but also have the important function of housing many critical pieces if equipment. Interior spaces between the ribs and spars inside the wing, called wingboxes, house things like fuel lines, hydraulic pumps, electrical wires, hoses, etc. Above all other things, the structure and aerodynamics of the wings are crucial for safe and efficient operation of the aircraft. Unfortunately, there are ergonomic constraints introduced by the need for humans to access the inside of the wingboxes in order for assembly and maintenance to occur. To meet these ergonomic constraints, Boeing has had to cut access holes in the outside skin of the wing, as well as modify the interior spaces to be more human accessible. These two things both compromise the structural integrity and decrease the aerodynamic efficiency of the wings.

Boeing is therefore very interested in developing a robotic system that could operate inside the wing to assist with assembly and maintenance tasks. This system would remove the ergonomic constraints, as it could operate in much smaller spaces. It would also carry with it the benefits inherent to robotics: increased speed, repeatability and accuracy during assembly and maintenance.

<br>
<br>

##Simulation and Control

My capstone team was tasked to develop a simulation and control system for a robot designed to operate inside an aircraft wing. In addition to being the the team leader, I also wrote all the code for the simulator and the control system as other members of the team were not familiar with programming. The general architecture of the system was split into three parts: a client, server and the simulation data.

<br>
<br>

<center>
<img src="{{wr}}static/img/wingbox/sc14.png" class="thumbnail" width="99%">

Screenshot of the Client aligning to bolt holes.

</center>

<br>
<br>


General operation started out with the client to coordinate and control the robot. Using joysticks, renderings of the robot in its environment and a video feed, the operator could modify the client's simulation environment to be in some desired state. This state could then be sent to the server, which would do all the heavy computations necessary to smoothly and safely transition the robot from current state to the desired state. The server also did other computationally intensive tasks, such as object recognition of things like bolt holes, physics calculations, etc. Ultimately, the server was designed to control a physical robot, so an abstraction layer was developed to allow generic information from the simulation to be translated into hardware specific instructions. Support was also implemented between client and server to allow many clients to safely control a single robot. Finally, all the simulation data (descriptions of the kinematic bodies that comprise a robot, the location and contents of the simulation environment, etc) was kept separate to increase flexibility and portability of the software.

<br>
<br>

##Conclusions

I am immensely proud of how the final product turned out and had a ton of fun working with RPI and Boeing on the project. There are two things I wish I could change though with this project.

First, I either wish that I wasn't team leader so I could spend more time coding, or someone else on the team also could have also coded along side me. I just felt spread too thin between coding this massive application and also being a manager. I would rather do one thing and do it well as opposed to do two or more things and not be able to give each my best.

Second, I can't show any of my work off! This is probably the biggest and best engineered piece software I've written. All the intellectual property is technically owned by RPI / Boeing, so I can't release any of it. In the future I'd like to get permission to gut out any proprietary information, polish a few things up and release it as a collaborative robot planning tool.

<br>
<br>

##Shout outs

My capstone team: Sairina Mirchandani, Amber Mosal, Chris Low, Edward Shambeau and Sam Michon

From the RPI Design Lab: Casey Goodwin, Joshua Hurst and Mark Steiner for their excellent guidance, especially when it comes to the management side of things

Jamel Bland, Hillary Barr and Mark Goldhammer at Boeing for their technical input

Rosen Diankov for his assistance and OpenRAVE, one of the most awesome libraries I've worked with

{{disable comments}}
