import openFace
from openFace import string_clip
from RPLCD.i2c import CharLCD

lcd = CharLCD('PCF8574',address=0x27, port=1, cols=16, rows=2, dotsize=8)
openFace.cursor_position = [0,5]


lcd.clear()
bung = 'floopnorgsping'
print('huh')
string_clip(bung)

