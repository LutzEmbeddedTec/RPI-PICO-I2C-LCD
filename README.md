# RPI-PICO-I2C-LCD
This is a project which adapts code from another user to allow usage of the PCF8574 I2C lcd backpack for either 20x4 or 16x2 lcd screens.

Credit: https://github.com/dhylands/python_lcd/tree/master/lcd mostly to Dave Hylands for the basic api and lcd driver code.

Project: Check it out for a full step-by-setp guide on Instructables: https://www.instructables.com/RPI-Pico-I2C-LCD-Control/ 

This is code adaptded for micropython and the Raspberry Pi PICO specifically.

# Detailed explanation in the video

- copy files to raspberry pico
- run main.scan.py and read I2C Adress
- run pico_i2c_lcd_test.py

Requirements:
- 3.3 - 5V level translator. This is crucial to encure the lcd recieves the commands properly. I recommend this: https://www.adafruit.com/product/757 (Must be Bi-Directional)
- PCF8574 I2C LCD backpack. (These are common to find)

Functions / Usage: 

These are the python commands used in a program! (They can all be found in the lcd_api.py file with definitions to their functions)
- lcd.putstr("Text goes here!")                     - Send a string of chars to the display IMPORTANT: Use this for printing a variable: lcd.putstr(str(Variable)) [Turns variable into string] 
- lcd.show_cursor() / lcd.hide_cursor()             - Show / Hide the cursor of the lcd (White bar)
- lcd.blink_cursor_on() / lcd.blink_cursor_off()    - Turn on / Off the blinking cursor upon printing
- lcd.backlight_on() / lcd.backlight_off()          - Turn on / Off backlight of the LCD (Controlled by a small transistor on the backpack)
- lcd.display_on() / lcd.display_off()              - Turn on / Off the display (Not backlight but the entire chip)
- lcd.clear()                                       - Clear all chars or anything written to the display
- lcd.move_to(Col, Row)                             - Move to position based on row and col values (Y, X)
- lcd.custom_char(Num, bytearray([HEX chars])))     - Num can be any integer 0 - 8 (Writing to CGRAM locations) merely used for numbering. The HEX chars are simply made by using this link: https://maxpromer.github.io/LCD-Character-Creator/. It will provide a string of Hex charecters which can replace the "HEX chars" in the example command.
- lcd.write_line(String, Linie)                     - Writes a string to a defines line

