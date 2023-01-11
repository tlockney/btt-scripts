tell application "zoom.us" to activate
tell application "System Events" to tell application process "zoom.us"
    if exists (menu bar item "Window" of menu bar 1) then
      click (menu item "Close" of menu 1 of menu bar item "Window" of menu bar 1)
      delay 0.5
      click button 1 of window 1
    end if
end tell
