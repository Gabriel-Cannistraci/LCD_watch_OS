from RPLCD.i2c import CharLCD
from gpiozero import Button
from signal import pause
from time import sleep
import random

#personal high score 874

lcd = CharLCD('PCF8574',address=0x27, port=1, cols=16, rows=2, dotsize=8)

button = Button(13)

sleep(1)

dinoChar = (
    0b01100,
    0b01111,
    0b00100,
    0b00111,
    0b01110,
    0b11100,
    0b10010,
    0b11011,)

lcd.create_char(0,dinoChar)

cactus = (
    0b00101,
    0b00101,
    0b10111,
    0b10100,
    0b10100,
    0b11101,
    0b00111,
    0b00100,)

lcd.create_char(1,cactus)

ptero = (
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b01000,
    0b11111,
    0b00110,
    0b00010,)

lcd.create_char(2,ptero)

blank = (
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000)
lcd.create_char(3,blank)

#lcd.write(1)
#lcd.write(2)
#lcd.cursor_pos = (1,0)
#lcd.write(0)

jump = False
jumpT = 0
run = True

enemies = []
hscore = 0

def spawn(vari):
    Enem = enemy(vari)
    enemies.append(Enem)

def getCoords(pos):
    coor1 = pos[0]
    coor2 = pos[1]
    return(coor1,coor2)


class dino:
    def __init__(self,pos,run,jump):
        self.pos = pos
        self.run = run
        self.jump = jump
        self.airTime = 0 
        
    def coords(self):
        #how far down
        coor1 = self.pos[0]
        #how far across
        coor2 = self.pos[1]
        return (coor1, coor2)
        
    def pos_clear(self):
    #clears the full square at one location
        #change self.coords if no working may mess it up
        lcd.cursor_pos = (self.coords())
        lcd.write(3)
        #print('clear')

    def makeDino(self):
        lcd.cursor_pos = (self.pos)
        lcd.write(0)
        #print('make')

    def down(self):
#     makes player run on bottom
        if self.run != True or self.jump == True:
            self.pos_clear()
            self.run = True
            self.jump = False
            self.pos[0] = 1
            self.makeDino()
    
    def up(self):
        self.airTime += 1
        if self.jump != True:
            self.pos_clear()
            self.jump = True
            self.run = False
            self.pos[0] = 0
            self.makeDino()
            self.checkUp()
        #print('jump')
        
    def checkUp(self):
        if self.airTime > 6:
            self.down()
            self.airTime = 0
            return True
        else:
            return False
          
class enemy:
    def __init__(self, vari):
        
        self.vari = vari
        if vari == 2:
            self.pos = [0,15]
        else:
            self.pos = [1,15]
        
    def pos_clear(self):
    #clears the full square at one location
        #change self.coords if no working may mess it up
        lcd.cursor_pos = (self.coords())
        lcd.write(3)
        #print('clear')
            
    def coords(self):
        #how far down
        coor1 = self.pos[0]
        #how far across
        coor2 = self.pos[1]
        return (coor1, coor2)
           
    def make(self):
        lcd.cursor_pos = (self.coords())
        lcd.write(self.vari)
        #print('make')
           
    def move(self):
        self.pos_clear()
        if self.pos[1] > 0:
            self.pos[1] -= 1
            self.make()
        elif self in enemies:
            enemies.remove(self)
    
def is_touch():
    for enemy in enemies:
        if player.pos == enemy.pos:
            return True

player = dino([1,0],True,False)
score = 0
running = True
def start():
    lcd.write_string("Dino Time")
    sleep(0.9)
    lcd.clear()
    sleep(0.2)
    player.pos[0] = 1
    player.makeDino()
    sleep(1)
    begin()

def begin():
    frames = 0
    spawnable = False
    running = True
    
    while running:
        sleep(0.06)
        frames += 1
        player.makeDino()
        if (button.is_pressed or player.jump == True) and player.checkUp() != True:
            player.up()
            #print('jump')
            
        else:
            player.down()
            #print('down')
        
        spawnish = random.randint(0,3)
        #print("trying spawn")
        var1 = 0
        var2 = 0
        if spawnish == 1 and frames > 15:
            if len(enemies) > 0:
                for en in enemies:
                    if en.vari == 1:
                        var1 += 1
                    if en.vari == 2:
                        var2 +=2
                    for i in range(0,1):
                        for y in range(15,11, -1):
                            if en.pos[0] != i and en.pos[1] != y:
                                #print('yay')
                                spawnable = True
                            else:
                                spawnable = False
                                #print('nay')
                                break
            else:
                spawnable = True
        if spawnable == True:
            yes = random.randint(0,2)
            if yes == 2 and var2 <= 2:
                spawn(2)
            elif var1 < 4:
                spawn(1)
            spawnable = False
        
        for en in enemies:
            en.move()
        
        if is_touch() == True:
            die(frames)
            running = False
        
def die(score):
    global hscore
    for enim in (enemies):
        enemies.remove(enim)
        
    for enim in enemies:
        enemies.remove(enim)
    
    lcd.clear()
    lcd.write_string(f'Bro died! \n\rFinal score: {score}')
    num = 0
    if score > hscore:
        hscore = score
        button.wait_for_press(timeout = 10)
        lcd.clear()
        print('huh')
        lcd.write_string(f'New High score: {hscore}!')
        sleep(1)
                
    button.wait_for_press(timeout = 10)
    while num < 50:
        if button.is_pressed:
            print("pressed")
            lcd.clear()
            sleep(0.01)
            start()
            break
        else:
            num += 1
        sleep(0.01)
   
start()
lcd.clear()
lcd.write_string(f'The end! \n\rHigh score: {hscore}')
