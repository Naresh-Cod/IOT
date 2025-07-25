int segmentPins[] = {2, 3, 4, 5, 6, 7, 8}; // a, b, c, d, e, f, g
int digitPins[] = {10, 11, 12, 13};        // digit 1 to 4

// 0-9 segment patterns (a-g)
byte digits[10] = {
  B00111111, // 0
  B00000110, // 1
  B01011011, // 2
  B01001111, // 3
  B01100110, // 4
  B01101101, // 5
  B01111101, // 6
  B00000111, // 7
  B01111111, // 8
  B01101111  // 9
};

void setup() {
  for (int i = 0; i < 7; i++) pinMode(segmentPins[i], OUTPUT);
  for (int i = 0; i < 4; i++) pinMode(digitPins[i], OUTPUT);
}

void loop() {
  int number[4] = {1, 2, 3, 4}; // Number to display
  for (int i = 0; i < 4; i++) {
    displayDigit(number[i], i);
    delay(5); // Multiplex delay
  }
}

void displayDigit(int num, int digit) {
  // Turn off all digits
  for (int i = 0; i < 4; i++) digitalWrite(digitPins[i], HIGH);
  
  // Set segment pattern
  for (int j = 0; j < 7; j++) {
    digitalWrite(segmentPins[j], bitRead(digits[num], j));
  }

  // Enable current digit (active LOW)
  digitalWrite(digitPins[digit], LOW);
}
