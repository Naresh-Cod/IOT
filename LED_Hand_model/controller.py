from pyfirmata import Arduino

class LEDController:
    def __init__(self, port='/dev/ttyACM0'):
        self.board = Arduino(port)
        self.led_pins = {
            1: self.board.get_pin('d:8:o'),   # Red
            2: self.board.get_pin('d:9:o'),   # Green
            3: self.board.get_pin('d:10:o'),  # White
            4: self.board.get_pin('d:11:o'),  # Blue
            5: self.board.get_pin('d:12:o')   # Yellow
        }

    def turn_on_led(self, finger_count):
        self.turn_off_all()
        if finger_count in self.led_pins:
            self.led_pins[finger_count].write(1)

    def turn_off_all(self):
        for pin in self.led_pins.values():
            pin.write(0)
