set zoomStatus to false
set micStatus to false
set callStatus to false
set videoStatus to false
set shareStatus to false
set recordStatus to false

tell application "System Events"
	if exists (window 1 of process "zoom.us") then
		set zoomStatus to true
		tell application process "zoom.us"
			if exists (menu bar item "Meeting" of menu bar 1) then
				set callStatus to true
				if exists (menu item "Mute Audio" of menu 1 of menu bar item "Meeting" of menu bar 1) then
					set micStatus to true
				else
					set micStatus to false
				end if
				if exists (menu item "Start Video" of menu 1 of menu bar item "Meeting" of menu bar 1) then
					set videoStatus to false
				else
					set videoStatus to true
				end if
				if exists (menu item "Start Share" of menu 1 of menu bar item "Meeting" of menu bar 1) then
					set shareStatus to false
				else
					set shareStatus to true
				end if
				if exists (menu item "Record to the Cloud" of menu 1 of menu bar item "Meeting" of menu bar 1) then
					set recordStatus to false
				else if exists (menu item "Record" of menu 1 of menu bar item "Meeting" of menu bar 1) then
					set recordStatus to false
				else
					set recordStatus to true
				end if
			end if
		end tell
	end if
end tell

-- return {zoom:zoomStatus, inMeeting:callStatus}
return {zoom:zoomStatus, inMeeting:callStatus, micOn:micStatus, videoOn:videoStatus, isSharing:shareStatus, isRecording:recordStatus }
