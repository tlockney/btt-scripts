tell application "System Events" to tell process "zoom.us"
    if exists (menu item "Unmute Audio" of menu 1 of menu bar item "Meeting" of menu bar 1) then
        click (menu item "Unmute Audio" of menu 1 of menu bar item "Meeting" of menu bar 1)
    else
        click (menu item "Mute Audio" of menu 1 of menu bar item "Meeting" of menu bar 1)
    end if
end tell
