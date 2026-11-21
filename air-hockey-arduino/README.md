Air Hockey Using Arduino

An Arduino-based air hockey table. The Arduino Uno coordinates gameplay, while an air blower helps the puck glide, servo motors control paddle movement, and a 16×2 LCD displays scores and game information.
Features
- Arduino Uno-based control
- Air blower/fan for puck movement
- Servo motors for paddle actuation
- Sensors for puck detection
- 16×2 LCD for score display
- Two-player gameplay
  
Components
- Arduino Uno
- 16×2 LCD
- Servo motors / paddle actuators
- Air blower or fan
- Sensors and pushbuttons
- Puck, mallets, jumper wires, and power supply
- Playing surface and table frame
  
Software
- Arduino IDE
- Arduino LiquidCrystal library
  
LCD Connections
Example 4-bit connections from the project report:
LCD pin	Arduino
VSS / VDD	GND / 5V
VO	Potentiometer wiper
RS / RW	Digital 12 / GND
E	Digital 11
D4–D7	Digital 5, 4, 3, 2
A / K	5V / GND (backlight)


Verify all connections against your actual circuit before powering the project.

Working
1. The blower sends air through holes in the playing surface to reduce puck friction.
2. Players use mallets to hit the puck toward the opponent's goal.
3. Arduino reads sensor and control inputs and coordinates the hardware.
4. The LCD displays scores and game information.
   
Setup
1. Assemble the table, playing surface, goals, and frame.
2. Install the blower, actuators, sensors, LCD, and controls.
3. Connect components according to the circuit diagram.
4. Open the Arduino sketch in Arduino IDE.
5. Select the board and port, then compile and upload the code.
6. Test airflow, paddles, sensors, LCD, and scoring.
