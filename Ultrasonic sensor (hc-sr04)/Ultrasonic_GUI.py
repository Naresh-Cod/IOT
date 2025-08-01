import tkinter as tk
import math
import serial
import threading

SERIAL_PORT = "/dev/ttyACM0"  # change as needed
BAUD_RATE = 9600

class RadarGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Ultrasonic Radar GUI")
        self.root.geometry("600x600")
        self.canvas = tk.Canvas(root, bg='black', width=600, height=600)
        self.canvas.pack()

        self.center = (300, 300)
        self.radius = 250
        self.angle = 0
        self.distance = 0

        self.serial = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        threading.Thread(target=self.read_serial, daemon=True).start()
        self.update_radar()

    def read_serial(self):
        while True:
            try:
                line = self.serial.readline().decode().strip()
                if line:
                    self.distance = float(line)
            except:
                continue

    def update_radar(self):
        self.canvas.delete("all")

        # Draw semi-circles and center lines
        for r in range(50, 301, 50):
            self.canvas.create_arc(
                self.center[0]-r, self.center[1]-r,
                self.center[0]+r, self.center[1]+r,
                start=0, extent=180, outline="green"
            )

        for a in range(0, 181, 30):
            x = self.center[0] + self.radius * math.cos(math.radians(a))
            y = self.center[1] - self.radius * math.sin(math.radians(a))
            self.canvas.create_line(self.center[0], self.center[1], x, y, fill="green")

        # Rotate line
        x = self.center[0] + self.radius * math.cos(math.radians(self.angle))
        y = self.center[1] - self.radius * math.sin(math.radians(self.angle))
        self.canvas.create_line(self.center[0], self.center[1], x, y, fill="lime", width=2)

        # Draw object if in range
        if self.distance > 2 and self.distance < 300:
            r = min(self.distance, 250)
            ox = self.center[0] + r * math.cos(math.radians(self.angle))
            oy = self.center[1] - r * math.sin(math.radians(self.angle))
            self.canvas.create_oval(ox-5, oy-5, ox+5, oy+5, fill="red")

        # Update angle
        self.angle += 1
        if self.angle > 180:
            self.angle = 0

        self.root.after(50, self.update_radar)

# Start GUI
root = tk.Tk()
app = RadarGUI(root)
root.mainloop()

