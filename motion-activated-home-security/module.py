
import cv2
import time
import RPi.GPIO as GPIO
from smbus import SMBus

# GPIO setup for PIR sensor
PIR_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

# LCD I2C setup
I2C_ADDR = 0x27  # Change this to your LCD's I2C address
LCD_WIDTH = 16   # Adjust for 16x2 or 20x4 LCD
bus = SMBus(1)

# LCD Constants
LCD_CHR = 1
LCD_CMD = 0
LINE_1 = 0x80
LINE_2 = 0xC0
ENABLE = 0b00000100
BACKLIGHT = 0x08


def lcd_init():
    lcd_byte(0x33, LCD_CMD)  # Initialize
    lcd_byte(0x32, LCD_CMD)  # Set to 4-bit mode
    lcd_byte(0x06, LCD_CMD)  # Cursor move direction
    lcd_byte(0x0C, LCD_CMD)  # Turn cursor off
    lcd_byte(0x28, LCD_CMD)  # 2-line display
    lcd_byte(0x01, LCD_CMD)  # Clear display
    time.sleep(0.05)


def lcd_byte(bits, mode):
    bits_high = mode | (bits & 0xF0) | BACKLIGHT
    bits_low = mode | ((bits << 4) & 0xF0) | BACKLIGHT
    bus.write_byte(I2C_ADDR, bits_high)
    lcd_toggle_enable(bits_high)
    bus.write_byte(I2C_ADDR, bits_low)
    lcd_toggle_enable(bits_low)


def lcd_toggle_enable(bits):
    time.sleep(0.0005)
    bus.write_byte(I2C_ADDR, (bits | ENABLE))
    time.sleep(0.0005)
    bus.write_byte(I2C_ADDR, (bits & ~ENABLE))
    time.sleep(0.0005)


def lcd_message(message, line):
    lcd_byte(line, LCD_CMD)
    for char in message.ljust(LCD_WIDTH):
        lcd_byte(ord(char), LCD_CHR)


# Initialize LCD
lcd_init()
lcd_message("System Starting", LINE_1)
time.sleep(2)
lcd_message("Ready", LINE_1)

# Video capture setup
camera = cv2.VideoCapture(0)  # Use USB camera
frame_width = int(camera.get(3))
frame_height = int(camera.get(4))
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Duration of recording after motion is detected
RECORD_SECONDS = 10

try:
    while True:
        if GPIO.input(PIR_PIN):  # Motion detected
            lcd_message("Motion Detected", LINE_1)
            lcd_message("Recording...", LINE_2)
            print("Motion detected! Starting video recording.")
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            video_filename = f"/home/pi/Videos/{timestamp}.avi"
            out = cv2.VideoWriter(video_filename, fourcc, 20.0, (frame_width, frame_height))

            start_time = time.time()
            while time.time() - start_time < RECORD_SECONDS:
                ret, frame = camera.read()
                if ret:
                    out.write(frame)
                else:
                    print("Failed to capture frame.")
                    break

            out.release()
            print(f"Video saved: {video_filename}")
            lcd_message("Recording Done", LINE_1)
            lcd_message("Ready", LINE_2)
            time.sleep(5)  # Cooldown before next detection
        else:
            time.sleep(0.1)  # Check periodically

except KeyboardInterrupt:
    print("Program terminated by user.")
    lcd_message("Shutting Down", LINE_1)
    time.sleep(2)

finally:
    GPIO.cleanup()
    camera.release()
    cv2.destroyAllWindows()
    lcd_message("Goodbye!", LINE_1)
