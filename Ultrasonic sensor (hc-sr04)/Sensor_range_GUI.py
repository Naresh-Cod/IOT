import tkinter as tk
from tkinter import ttk
import serial
import threading

# Update the serial port name according to your system
# Eg: COM3 for Windows or /dev/ttyUSB0 for Linux
SERIAL_PORT = "/dev/ttyUSB0"
BAUD_RATE = 9600

class DistanceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Ultrasonic Distance Sensor (HC-SR04)")
        self.root.geometry("400x200")
        self.root.configure(bg="#222")

        self.label = tk.Label(root, text="Distance:", font=("Helvetica", 20), fg="white", bg="#222")
        self.label.pack(pady=10)

        self.distance_var = tk.StringVar()
        self.distance_display = tk.Label(root, textvariable=self.distance_var, font=("Helvetica", 36), fg="#00ff00", bg="#222")
        self.distance_display.pack()

        self.progress = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate', maximum=200)
        self.progress.pack(pady=20)

        self.serial_connection = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        self.read_serial_thread()

    def read_serial_thread(self):
        def task():
            while True:
                try:
                    line = self.serial_connection.readline().decode('utf-8').strip()
                    if line:
                        distance = float(line)
                        self.distance_var.set(f"{distance:.2f} cm")
                        self.progress['value'] = min(distance, 200)
                except:
                    pass

        threading.Thread(target=task, daemon=True).start()

# Run GUI
root = tk.Tk()
app = DistanceGUI(root)
root.mainloop()

