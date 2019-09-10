#this Script will create a Progress Bar
#The Progress will be Manually Updated using the format listed below
#progress_bar.UpdateBar(Value of Bar, Maximum Bar Value)
#the Window uses a .Finalize Function to make the window Persistent
 
#Import the PySimpleGUI Library
import PySimpleGUI as sg
#Import the Time Library for use in this script
import time
 
#this is for the Layout Design of the Window
layout = [[sg.Text('Custom Text')],
              [sg.ProgressBar(1, orientation='h', size=(20, 20), key='progress')],
          ]
#This Creates the Physical Window
window = sg.Window('Window Title', layout).Finalize()
progress_bar = window.FindElement('progress')
 
#This Updates the Window
#progress_bar.UpdateBar(Current Value to show, Maximum Value to show)
progress_bar.UpdateBar(0, 5)
#adding time.sleep(length in Seconds) has been used to Simulate adding your script in between Bar Updates
time.sleep(.5)
 
progress_bar.UpdateBar(1, 5)
time.sleep(.5)
 
progress_bar.UpdateBar(2, 5)
time.sleep(.5)
 
progress_bar.UpdateBar(3, 5)
time.sleep(.5)
 
progress_bar.UpdateBar(4, 5)
time.sleep(.5)
 
progress_bar.UpdateBar(5, 5)
time.sleep(.5)
#I paused for 3 seconds at the end to give you time to see it has completed before closing the window
time.sleep(3)
 
#This will Close The Window
window.Close()
 
#Thanks for Using PySimpleGUI