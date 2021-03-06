#Harvard - Smithsonian Center for Astrophysics
##Automated Multilayer Fabrication

<center>
<img src="{{wr}}static/img/chamber.png" class="thumbnail" width="66%">
</center>
<br>

##Overview

For the past two and a half years I have worked at the [Harvard-Smithsonian Center for Astrophysics](http://www.cfa.harvard.edu/hea/). I have had the distinct pleasure of working with Dr. Suzanne Romaine and Ricardo Bruni integrating hardware and writing software that automates the fabrication of multilayer (and sometimes non-multilayer) coatings on the surfaces of optics to be used for X-ray imaging (mostly in astronomy).

For astronomy, these multilayer coatings are designed to capture, focus and reflect the X-ray photons from deep space back on to an array of detectors inside of the telescope to form an image. The coatings are called "multilayers" because they consist of very thin (sometimes only a couple of angstroms) alternating layers of different materials (They are essentially man-made bragg crystals).

My time at Harvard-CFA has been tremendously valuable to me. While there, I have:

- Honed my troubleshooting and analytical problem solving abilities
- Developed strong communication skills by working with astrophysicists, engineers, hardware vendors, etc.
- Gained valuable technical experience with automation, programming, engineering, astrophysics, materials science and more

My major accomplishment at Harvard has been writing a software suite to automate the complex task of creating an optic given specific geometry, thicknesses, and various other parameters. Along the journey of implementing this software, I have had to develop a fairly complex UI, control sequences, hardware monitors, error checkers and motion control algorithms. One of the most challenging parts has been the program's organization. As the complexity of the programs have increased, I've had to rework the architecture several times to increase efficiency, eliminate redundant code, and ultimately make the whole application much tighter, portable and friendly to use and develop. The utilities I wrote also allow me to monitor and control chamber hardware without being physically present in the lab (extremely valuable for troubleshooting from home or out of state).

<br>
<br>

<center>
<img src="{{wr}}static/img/screen.jpg" class="thumbnail" width="84%">

</center>
<small>
**Multilayer Fabrication Software**: The gray window is for production runs, the blue window is for manually controlling chamber hardware, and the yellow window displays the state of the chamber.
</small>

<br>
<br>

Ultimately the end result has been the creation of a robust and easy to use system that makes the daunting task of producing any kind of X-ray optic as easy and stress free as possible for someone not intimately familiar with the details. Hopefully if NASA ever gets enough funding, my tools will end up creating something that ends up in space!

<br>
<br>

##About Multilayer Fabrication

The software I have written works off a list of desired layer thicknesses. The user can either use the program to generate constant thicknesses itself, or alternatively can choose to import a list of thicknesses generated by another program (such as thicknesses generated from a program in [IDL](http://www.ittvis.com/ProductServices/IDL.aspx), Matlab, etc). The user then inputs a few other parameters, such as the number of layers and the material deposition rates. Once all the pre-run parameters are entered, the program generates a set of instructions for itself to follow during the run. All input and instructions are checked for potential errors, and if everything checks out the user can start the run.

The technique used to actually coat the optic is called DC magnetron sputtering. A really good explainaion of the basics can be found [here](http://www.ajaint.com/whatis.htm). This technique, in combination with other constraints for the multilayer dictate the following basic requirements:

- The coating is conducted in a vacuum chamber
- Deposition rates of materials are held constant within a fixed cross section
- Since sputter cross section and optic substrate are different sizes, the position of the substrate needs to move around inside the chamber in order to get an even deposition.
- Substrate also needs to be able to move between two sources to form a multilayer

The deposition sources (magnetrons, also called the cathodes) are always on during a run, can only deposit one material at a fixed rate, and only cover a small portion of the total surface on the optic to be coated. Therefore, I hat to write control algorithms to determine how to move equipment inside the chamber to properly and accurately coat the optic evenly. The basic equipment I had at my disposal to achieve this level of control are:

- A four axis stepper motor controller in the PC (instructions are issued to it by software)
- A stepper motor attached to the platen, used for angular positioning of the optic about the center of the chamber
- Two shutters to block or allow sputter to flow from a source's magnetron
- An optional mandrel (also controlled VIA a vacuum rated stepper) to add an extra dimension to coatings (IE coat a cylindrical optic as opposed to a flat wafer)
- Stepper motor drivers to actually power and actuate stepper motors based on commands from the controller in the PC
- Assorted power supplies and instruments to monitor temperature, flow rate, etc.

Once a run is started, the user sits back and monitors the chamber and magnetron conditions while the coating is executed. Multilayers can be several hundred angstroms thick and deposition rates are small, so its not rare that a run lasts several hours. In the event of an emergency or if something needs to be re-adjusted, the user can choose to abort or pause a run. While paused or not in a run, a full suite of tools to manually control and re-align the chamber are available. At all times, the user has graphical feedback as to the current status of the chamber, as well as how far along the run has progressed.

<br>
<br>

##Other Work

Further work I've done at Harvard includes:

- Unifying all versions of the software for all the different chambers and optic geometries (there used to be a separate version for each, made maintenance a nightmare)
- Designing chamber hardware from CAD (including a portable stand for a vacuum chamber that weighed several hundred pounds)
- Ordering the fabrication of parts through machinists
- Chamber assembly
- Supervising a high school student for a summer
- Fixing a $70,000 profile-meter used for substrate characterizations
- Decreased shutter latency and saved money by designing a cheap solenoid controller
- Helped with data distribution for an experiment run at Brookhaven National Laboratory
- Probably more things that I am forgetting about.

{{disable comments}}
