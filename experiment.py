from psychopy import visual, core, event
from loom import *

# display = pyglet.canvas.get_display()
# screens = display.get_screens()
# screenSize = [screens[0].width, screens[0].height]

# Window
win = visual.Window(monitor="testMonitor", fullscr=True, units="deg", allowGUI=False, color=(1, 1, 1), colorSpace='rgb')
event.Mouse(visible=False)


# Run experiment
exp = loom(win=win, size=10, expTime=3, iti=10, stimColor='black')
exp.play()

# Cleanup			
win.close()
core.quit()