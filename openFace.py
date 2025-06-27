from RPLCD.i2c import CharLCD
from gpiozero import RotaryEncoder,Button, DigitalInputDevice
from signal import pause
from time import sleep, strftime
from threading import Event
from datetime import datetime

encoder = RotaryEncoder(a=26,b=19)
but1 = Button(5, hold_time=1.5)
but_en = Button(13) #encoders button
lcd = CharLCD('PCF8574',address=0x27, port=1, cols=16, rows=2, dotsize=8)

stop_event = Event()
context = ""
cursor_position = [0,6]
presses = 0 # to make sure in button press that when long press is registered...
#...short press isn't registered 
faceOn = True


def doExit():
    print('exit')
    stop_event.set()
def doExitlong():
    print('long')
    
dispatch = {
    ('faceloop', 'short'): doExit, 
    ('faceloop', 'long'): doExitlong,
   #('context or where you are','button press time'): function it does
    #(put context at beginning of any new face/app/etc )
    }

def but1pres(time): #this is shit code, no clue how to fix it
    global presses #does this to make sure short press not registered after long one
    print('huh')
    if time == 'long':
        presses = 1
    if presses == 1 and time == 'short':
        presses = 0
        return
    action = dispatch.get((context,time))
    #print(f'{context}, {time}')
    if action:
        #print('what')
        action()
     
but1.when_held = lambda: but1pres('long')
but1.when_released = lambda: but1pres('short')

def string_clip(string):
    global cursor_position
    for letter in string:
        if cursor_position[1] < 16:
            lcd.cursor_pos = (cursor_position[0],cursor_position[1])
            lcd.write_string(letter)
            cursor_position[1] += 1
        else:
            break
            cursor_position[1] = 0


"""def face():
    
    while not stop_event.is_set():
        faceOn = True #check this make sure it can be here
        
   
   """     


def clock(): #first main loop 
    global context
    global cursor_position
    global faceOn
    Pocr = {'start': [0,0],#start [1] no more than 4 or else goes to bottom screen
            'I': [0,0],
            'M': [0,0],
            'S': [0,0],
            'P': [0,0]} #POsition of CuRsor variable
    Pocr['start'] = cursor_position.copy()
    last = {'I': '','M': '','S': '', 'P': ''}
    context = 'faceloop'
    try:
        while faceOn == True: #(set to not comment to test just clock) #not stop_event.is_set():
            for pos,coord in Pocr.items(): #this is to make sure it goes ahead if there is something before time
                Pocr[pos]=Pocr['start'].copy()
                #for value in coord:
                #print(pos,coord)
            i,m,s = strftime('%I:%M:%S').split(':')
            p = strftime('%p')
            if Pocr['start'][1] > 0:
                Pocr['I'][1] += 1
            if i != last['I']:
                cursor_position = Pocr['I'].copy(); string_clip(f'{i}:'); last['I'] = i;
            Pocr['M'] = Pocr['I'].copy()
            Pocr['M'][1] += 3 #change 3 if time format changes in a big way
            if m != last['M']:
                cursor_position = Pocr['M'].copy(); string_clip(f'{m}:'); last['M'] = m;
            #print(f'M{Pocr[M]}')
            Pocr['S'] = Pocr['M'].copy()
            Pocr['S'][1] += 3
            if s != last['S']:
                cursor_position = Pocr['S'].copy();string_clip(f'{s} '); last['S'] = s;
            #print(f'S{Pocr[S]}')
            #print(f'P{Pocr[P]}')
            Pocr['P'] = Pocr['S'].copy()
            Pocr['P'][1] += 3
            if p != last['P']:
                cursor_position = Pocr['P'].copy(); string_clip(p); last['P'] = p;
            cursor_position = Pocr['start'].copy()
            #with default hh:mm:ss pm, this whole thing takes 11 blocks (cursor spots)
            
            stop_event.wait(0.5)
    finally:
        print("Clock face ended")

if __name__ == '__main__':
    clock()


