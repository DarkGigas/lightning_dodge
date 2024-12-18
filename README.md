# lightning_dodge
I hate the Venus Sigil minigame

I'm running this on `Python 3.12.4`. Download it from [this link](https://www.python.org/downloads/);
This runs on windows, I haven't tried running it on Linux (I dont even know if the game can run on Linux, probably can)

To make this run sucessfully you will need to do a few steps with your game:
- Run on window mode, with a resolution big enough to fit your whole screen
- Play on mouse and keyboard (this might work with controller but I didnt test it out)
- You may run on the 2x Boost, but I didnt test it out on 4x Boost

Values you might wanna tweak if this doens't work perfectly:
- flash_threshold - this is set to 120 to ignore the clouds on the area as false positive, but you may wanna lower it to make it more sensitive or increase to make it less sensitive
- monitor_index - this is set to 1 which is usually your main monitor on Windows, you can change it if you are not playing on your main monitor
