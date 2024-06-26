# VRChat-OSC-Music-Control
This program is designed to be used with VRChat Parameters, and Voicemeeter. It has the ability to Pause/Play music playing on your PC, skip, and change the volume. 

## NOTICE
Currently, I am just publishing this here as-is, and how I use it. In the future I may develop a more user-friendly version, but for now its the code, and the code only.

# How to install
## PC SIDE
1. Install Python (if not done already)
2. Install all the libraries in command prompt:<br/>
   `pip install argparse` <br/>
   `pip install pynput`<br/>
   `pip install python-osc`<br/>
3. Install OSC2MEETER (for Voicemeeter volume control) from `https://github.com/TheStaticTurtle/OSC2MEETER`
## AVATAR SIDE
1. Create 3 parameters in the FX Animator:<br/>
  `musictoggle`<br/>
  `musicskip`<br/>
  `volume0`<br/>
2. For radial menu controls, create 3 parameters of the same name in your avatar parameters.
3. Create 2 buttons in the expressions menu (submenu works too), one with the `musictoggle` parameter, and the other with the `musicskip` parameter.
4. For volume control (Voicemeeter Potato required), create a Radial Puppet in the expressions menu, with the parameter `volume0` attached to the Parameter Rotation of that Radial Puppet.<br/>
At this point, everything should function, and if you know how, contacts also work really well for the control system.
Thank you for using my program, and I hope you enjoy it! 
