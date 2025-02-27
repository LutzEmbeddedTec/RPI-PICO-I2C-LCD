import machine
from machine import I2C
from time import sleep
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20


i2c = I2C(1, sda=machine.Pin(14), scl=machine.Pin(15), freq=100000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)


lcd.display_on()
sleep(1)
lcd.display_off()
sleep(1)
lcd.backlight_off()
sleep(1)
lcd.backlight_on()
sleep(1)
lcd.blink_cursor_on()
sleep(1)
lcd.blink_cursor_off()
sleep(1)
lcd.clear()


# lcd.custom_char(0, bytearray([  0x00,  0x00,  0x00,  0x01,  0x03,  0x16,  0x1C,  0x08]))
# 
# lcd.custom_char(1, bytearray([ 0x10,  0x18,  0x1C,  0x1E,  0x1C,  0x18,  0x10,  0x00]))
# 
# lcd.putchar(chr(0))
# 
# lcd.write_line("Lutz embedded Tec ",0)
# lcd.write_line("      Intro ",1)
# lcd.write_line("      Connect",2)
# lcd.write_line("      Software",3)
# 
# 
# 
# for x in range(10):
#     lcd.move_to(13,1)
#     lcd.putchar(chr(0))
#     sleep(1)
#     lcd.move_to(13,1)
#     lcd.putchar(" ")
#     sleep(1)
#     
# lcd.move_to(5,2)
# lcd.putchar(chr(1))
