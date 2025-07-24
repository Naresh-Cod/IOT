int segmentPins[] = {2, 3, 4, 5, 6, 7, 8}; // a to g

// 0-9 segment patterns (a-g, active HIGH)
byte numbers[10] = {
  B1111110, // 0
  B0110000, // 1
  B1101101, // 2
  B1111001, // 3
  B0110011, // 4
  B1011011, // 5
  B1011111, // 6
  B1110000, // 7
  B1111111, // 8
  B1111011  // 9
};

void setup() {
  for (int i = 0; i < 7; i++) {
    pinMode(segmentPins[i], OUTPUT);
  }
}

void loop() {
  for (int num = 0; num < 10; num++) {
    displayDigit(num);
    delay(1000);
  }
}

void displayDigit(int num) {
  for (int i = 0; i < 7; i++) {
    digitalWrite(segmentPins[i], bitRead(numbers[num], 6 - i)); // MSB first
  }
}
