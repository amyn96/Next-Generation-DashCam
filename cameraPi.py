import picamera
import RPi.GPIO as gpio
from time import sleep  
from subprocess import call
from datetime import datetime

from sendFile import sendFile, send_msg
from ip_location import ipLocation
from gps import GPSlocation

butstop=11 
butrecord=21 

HIGH=1
LOW=0

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(butstop, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(butrecord, gpio.IN, pull_up_down=gpio.PUD_DOWN)

user = "user2018402014"

#file name
timestr = datetime.now().strftime("%Y%m%d-%H%M%S")
vidname = user + "-" + timestr + ".h264"
imgname = user + "-" + timestr + ".jpg"

 
def record_video():
    print('Please Wait...')
    camera.start_preview()
    camera.start_recording(vidname)
    print('Recording started')
    

def stop_record():
    camera.stop_recording()
    camera.stop_preview()
    print('Video recorded successfully')
    print("We are going to convert the video.")
    # Define the command we want to execute.
    
    finvidname = user + "-" + timestr
    
    command = "MP4Box -add "+ vidname + " converted-" + finvidname + ".mp4"
    # Execute our command
    call([command], shell=True)
    # Video converted.
    print("Video converted.")
    sleep(2)
    print("Sending alert...")
    
    loc = ipLocation()
    gpsloc = GPSlocation()
    sendvidname = "converted-" + finvidname + ".mp4"
    msg = "User No. : " + user
    
    #print (sendvidname)
    
    if gpsloc:
        send_msg("An accident has Occured!!")
        send_msg(msg)
        sendFile(sendvidname, gpsloc)
    else :
        send_msg("An accident has Occured!!")
        send_msg(msg)
        sendFile(sendvidname, loc)
    #sendFile(sendvidname, loc)
    sleep(5)


def capture_image():
    print('Please Wait...')
    camera.start_preview()
    sleep(2)
    camera.capture(imgname)
    camera.stop_preview()
    print('Image Captured successfully')
    sleep(2)

print('Welcome to my System')
sleep(2)

print('Next-Generation DashCam Using IoT ')
sleep(3)

camera = picamera.PiCamera()
camera.awb_mode= 'auto'
camera.brightness=55

print(" Please Press Button")
sleep(2)

try:
    while 1:
        if gpio.input(butstop)==gpio.HIGH:
            print('Recording stoped')
            stop_record()
            sleep(2)
            print("Camera Turned Off...")
            sleep(5)
            exit(0)
        if gpio.input(butrecord)==gpio.HIGH:
            record_video()

        sleep(0.5)
        
except KeyboardInterrupt:
    print("Done........")
    sleep(3)
finally:
    exit(0)




