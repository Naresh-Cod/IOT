import serial
import pyautogui
import time

# Adjust your port and baud rate here:
arduino = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)  # Wait for connection

# Sensitivity settings
threshold = 0.5
speed = 10

while True:
    data = arduino.readline().decode().strip()  # Read from Arduino
    try:
        x_raw, y_raw, btn = map(int, data.split(","))
        x_move = 0
        y_move = 0

        if x_raw < 450:
            x_move = -speed
        elif x_raw > 550:
            x_move = speed

        if y_raw < 450:
            y_move = -speed
        elif y_raw > 550:
            y_move = speed

        pyautogui.moveRel(x_move, y_move)

        if btn == 0:  # Joystick pressed
            pyautogui.click()

    except Exception as e:
        print("Error:", e)
