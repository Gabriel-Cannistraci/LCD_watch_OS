An idea to turn a raspberry pi (pi 4 in my case), 2x16 or 4x16 lcd screen(see links section below), a button, and rotary encoder into a watch type device with hotswappable modules. 
This is an 'OS' for this watch. 
I want to make this as easy as possible for other people to add their own stuff for it.
I plan on making some videos to talk about the process and how it works.
I plan on making this readme doc better but I need to figure out how to do that.
This is not an actual OS in the sense it was built from the ground up, instead it is a framework for custom modules and applications for a pi with a screen.  

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Idea for physical layout: lcd and modules on wrist like a watch, connected to pi on bottom of wrist, all secured with bad or something idk. Will add images when they are made

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Notes for use: 
  -  needs gpiozero 1.6, get this by reinstalling it as gpiozero<2.0
  -  only tested on pi 4 (for now) but feel free to test on other stuff, it should work fine
  -  only tested on 2x16 lcd (for) must be one that uses 5x8 bits
  -  rotary encoder is implimented but has no use yet
  -  rotary encoder should be the one that can also be clicked from the top (ie. a second button )
  -  button uses: on clock face short press stops clock, will have long press just no use yet, jump in DinoRunner

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Current features:
  -  Clock (semi configurable), built so stuff can be added and changed later
  -  button press detector for long and short, had to do some weird work-around stuff to make it work, but it work
  -  DinoRunner game, based off of chrome no internet dino game, press button to jump, its pretty simple
  -  string_clip function that prints a string to screen, until it gets to the end of the screen then it stops, otherwise messes up line below

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Features to add:
  -  make long press configurable (customize time before a press is considered long), and later allow for multiple long press times, ie. one is 1.5 sec 2 is 2.5
  -  user input for configuration, through json (need to figrue out how to actually do that) and/or through shell outputs, basically allow people to add the necesary parts in any pins they want and more
  -  framework for custom 'apps'
  -  modules - like humiture sensor or whatever, inspired by this video from Zach Freedman https://www.youtube.com/watch?v=sxfJOMjZeIs&t=96s
  -  framework for custom modules
  -  files for 3d printing cases and whatnot, need to get my friend to make them, need to fix 3d printer so I can test them
  -  custom pcb files for custom modules and making the actual watch
  -  animation framework
  -  better custom characters, technically only 8 custom characters are allowed, but this will allow for more, maybe even a 'procedural generation' type of thing
  -  opening sequence which goes to configurable face (time, other info, 'app' quickstart)
  -  after opening sequence scrollable menu to choose 'app', and choose which module is added
  -  send signals direct to lcd pixels for even easier custom characters (maybe possible but probably not)
  -  limited web abilities, ie. connect to chatgpt
  -  vibration motor add on
  -  maybe add joystick support to be used instead of rotary encoder, or have both be available
  -  not a feature but make sure it works with pi zero for smaller form factor
  -  cooling somehow
  -  left and right handed support
    
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

App/module ideas
  -  music player, load on files and add on a speaker
  -  weather app, put humiture module, ir, barometer, shows you stats
  -  laser module
  -  echolocation app, use distance sensor to tell you how far away the wall is
  -  hall sensor (for fun idk)
  -  fishing game, stardew valley idea where to have to match hook with fish icon movement, just a bunch of quicktime events
  -  some game that uses outside sensors for stuff
  -  flipper zero type functionality, at least for some uses
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Notes for building your own stuff: 
  -  idk will figure out this stuff later
  -  2x16 lcd has built in symbols, they start at index 30(pretty sure) stop at 129(pretty sure) and start again in japanese at 160(pretty sure) then end at 255
  -  print symbols directly with lcd.write(<num>) (1-8 are custom ones) look in RPLCD docs below for more 

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Important links
  -  lcd use library RPLCD docs: https://rplcd.readthedocs.io/en/stable/index.html
  -  2x16 lcd specifications: https://cdn-shop.adafruit.com/datasheets/TC1602A-01T.pdf
  -  4x16 lcd specifications: https://cdn.sparkfun.com/assets/9/5/f/7/b/HD44780.pdf
  -  gpiozero docs: https://gpiozero.readthedocs.io/en/stable/index.html
  -  another helpful lcd spec doc: https://ecelabs.njit.edu/fed101/resources/LCD%20display%20on%20Arduino.pdf
