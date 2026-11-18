from tkinter import* # import everything from tkinter
from PIL import ImageTk,Image
import time # for sleep
from pyfirmata import Arduino,util
import subprocess
import serial
#import serial.tools.list_ports
import warnings
from multiprocessing import Process
import threading
#from decimal import Decimal

#Automatic arduino port searching
#arduino_ports = [p.device
#    for p in serial.tools.list_ports.comports()
#    if 'Arduino' in p.description]
#if not arduino_ports:
#    raise IOError("No Arduino found")
#if len(arduino_ports) > 1:
#    warnings.warn('Multiple Arduinos found - using the first')
#arduinoData = serial.Serial(arduino_ports[0], 9600, timeout=1)


#arduinoData = serial.Serial('COM4', 9600, timeout=1)

StopFill = 1
StopEmpty = 1
FillProcesses = 0
EmptyProcesses = 0
root = Tk() # the boxy window widget
root.title("Contact Angle Dispenser")

# for users to enter numbers  
StepsEntry = Entry(root, width=15, borderwidth = 5)
StepsEntry.grid(row=0, column=2)
StepsEntry.insert(2,"98")

SpeedEntry = Entry(root, width=15, borderwidth = 5)
SpeedEntry.grid(row=2, column=2)
SpeedEntry.insert(3,"1000")

FillEntry = Entry(root, width=15, borderwidth = 5)
FillEntry.grid(row=5, column=2)
FillEntry.insert(2,"10")
SetStepsLabel = Label(root, text = "rounds").grid(row=5, column = 3)

EmptyEntry = Entry(root, width=15, borderwidth = 5)
EmptyEntry.grid(row=6, column=2)
EmptyEntry.insert(2,"10")
SetStepsLabel = Label(root, text = "rounds").grid(row=6, column = 3)

#what happens after button is clicked
def Fill():
    global StopEmpty
    global StopFill
    global FillProcesses
    FillProcesses += 1
    StopEmpty = 0
    StopFill = 11
    Filling = threading.Thread(target=FillSubprocess)
    Filling.start()

def FillSubprocess():
    global StopEmpty
    global StopFill
    global FillProcesses
    x=1
    FillRounds = int(FillEntry.get())
    while StopFill != 0:
        if x <= FillRounds:
            #arduinoData.write(b'0')
            print('FillProcesses: ' + str(FillProcesses))
            print('EmptyProcesses: ' + str(EmptyProcesses))
            print('Filling' + str(x))
            x+=1
            time.sleep(2)
        if StopFill == 0:
            FillProcesses = 0
            break
        if FillProcesses > 1:
            FillProcesses = 1
            break

def Empty():
    global StopFill
    global StopEmpty
    global EmptyProcesses
    EmptyProcesses += 1
    StopEmpty = 111
    StopFill = 0
    Emptying = threading.Thread(target=EmptySubprocess)
    Emptying.start()
    
def EmptySubprocess():
    global StopFill
    global StopEmpty
    global EmptyProcesses
    y=1
    EmptyRounds = int(EmptyEntry.get())
    while StopEmpty != 0:
        if y <= EmptyRounds & StopEmpty!=0:
            #arduinoData.write(b'1')
            print('FillProcesses: ' + str(FillProcesses))
            print('EmptyProcesses: ' + str(EmptyProcesses))
            print('Emptying' + str(y))
            y+=1
            time.sleep(2)
        if StopEmpty == 0:
            EmptyProcesses = 0
            break
        if EmptyProcesses > 1:
            EmptyProcesses = 1
            break

def Steps():
    global Steps
    Stepss = str(8) + str(StepsEntry.get())
    ASteps = int(Stepss)
    BSteps = int(str(ASteps)[1:None])
    print (' Steps ' + str(BSteps))
    #arduinoData.write(ASteps.encode())    
    Func3 = Label(root, text = "Steps set to " + StepsEntry.get())
    Func3.grid(row=92, column=0, columnspan=3)

def Speed():
    global Speeds
    Speeds = str(9) + str(SpeedEntry.get())
    ASpeed = int(Speeds)
    BSpeed = int(str(ASpeed)[1:None])
    print (' Speed ' + str(BSpeed))
    #arduinoData.write(ASpeed.encode())
    Func4 = Label(root, text = "Speed set to " + SpeedEntry.get())
    Func4.grid(row=93, column=0, columnspan=3)

def Dispense():
    print('Dispensing')
    Speeding = threading.Thread(target = Speed)
    Speeding.start()
    Stepping = threading.Thread(target = Steps)
    Stepping.start()
    Stopping = threading.Thread(target = Stop)
    Stopping.start()
    #arduinoData.write(b'2')


def Stop():
    global StopFill
    global StopEmpty
    StopFill = 0
    StopEmpty = 0
    #arduinoData.write(b'3')
    
#default texts to be seen on widget
SetStepsButton = Button(root, text = "Set Steps", padx=10, command=Steps, bg="aqua", borderwidth = 3).grid(row=0, column = 1) 
SetStepsLabel = Label(root, text = "98 steps per drop").grid(row=1, column = 2) # label set to go into root window, grid for position
SetSpeedButton = Button(root, text = "Set Speed", padx=10  , command=Speed, bg="aqua", borderwidth = 3).grid(row=2, column = 1)
SetSpeedLabel = Label(root, text = "1K-5K").grid(row=3, column = 2)

EmptySpace1 = Label(root, text = "   ").grid(row=4, column = 2)

FillButton = Button(root, text = "Fill Syringe", padx=10, command = Fill, bg="yellow", borderwidth = 3).grid(row=5, column = 1)
EmptyButton = Button(root, text = "Empty Syringe", padx=10  , command = Empty, bg="yellow", borderwidth = 3).grid(row=6, column = 1)#bg=background fg=foreground

EmptySpace2= Label(root, text = "   ").grid(row=7, column = 2)
    
DispenseButton = Button(root,text = "Dispense", padx=28, pady=30, bg="lime", borderwidth = 5, command=Dispense, font=20).grid(row=8, column=1),# columnspan=2)
StopButton = Button(root,text = "Stop!!!!!", padx=28, pady=30, bg="Red", borderwidth = 5, command=Stop, font=20).grid(row=8, column=2),# columnspan=2)

root.mainloop()
