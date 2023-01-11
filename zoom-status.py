#!/usr/bin/env python3

from rich import print

import os
from subprocess import Popen, PIPE

def osascript(script):
    with Popen('osascript', stdin=PIPE, stdout=PIPE, stderr=PIPE) as process:
        stdout, _ = process.communicate(script.encode('utf-8'))
        return stdout.decode('utf-8').strip()

def get_status():
    out = osascript("""
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
        return {zoom:zoomStatus, inMeeting:callStatus, micOn:micStatus, videoOn:videoStatus, isSharing:shareStatus, isRecording:recordStatus}
    """)
    return dict(item.strip().split(':') for item in out.split(','))

def mute_audio():
    osascript('set volume with output muted')

def unmute_audio():
    osascript('set volume without output muted')

def audio_settings():
    out = osascript('get volume settings')
    # output volume:0, input volume:74, alert volume:100, output muted:true
    return dict(item.strip().replace(' ','_').split(':') for item in  out.split(','))

def toggle_mute():
    if audio_settings()['output_muted'] == 'true':
        unmute_audio()
    else:
        mute_audio()

def volume_up(inc):
    osascript(f"set volume output volume (output volume of (get volume settings) + {inc})")

def volume_down(inc):
    osascript(f"set volume output volume (output volume of (get volume settings) - {inc})")

def toggle(item):
    match item:
        case 'mic':
            menu_off, menu_on = ['Unmute Audio', 'Mute Audio']
        case 'video':
            menu_off, menu_on = ['Start Video', 'Stop Video']
        case 'share':
            menu_off, menu_on = ['Start Share', 'Stop Share']
        case 'record':
            menu_off, menu_on = ['Record', 'Stop Recording']
        case _:
            raise RuntimeError('No item specified.')
    osascript(f"""
        tell application "System Events" to tell application process "zoom.us"
            if exists (menu item "{menu_off}" of menu 1 of menu bar item "Meeting" of menu bar 1) then
                click (menu item "{menu_off}" of menu 1 of menu bar item "Meeting" of menu bar 1)
            else
                click (menu item "{menu_on}" of menu 1 of menu bar item "Meeting" of menu bar 1)
            end if
        end tell
    """)



if __name__ == '__main__':
    print(get_status())
    # toggle('video')
    # toggle_mute()
    # volume_down(10)
    print(audio_settings())
