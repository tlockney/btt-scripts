#!/usr/bin/env python3

import os
from subprocess import Popen, PIPE

# os.system("""
#     osascript << "APPLESCRIPT"
#     get volume settings
# APPLESCRIPT
# """)

def osascript(script):
    process = Popen('osascript', stdin=PIPE, stdout=PIPE, stderr=PIPE)
    out, _ = process.communicate(bytes(script, 'utf-8'))
    return out.decode('utf-8').strip()

# script = 'get volume settings'

script = """
tell application "System Events" to tell application process "zoom.us"
    if exists (menu item "Unmute Audio" of menu 1 of menu bar item "Meeting" of menu bar 1) then
        click (menu item "Unmute Audio" of menu 1 of menu bar item "Meeting" of menu bar 1)
    else
        click (menu item "Mute Audio" of menu 1 of menu bar item "Meeting" of menu bar 1)
    end if
end tell
"""
print(osascript(script))
