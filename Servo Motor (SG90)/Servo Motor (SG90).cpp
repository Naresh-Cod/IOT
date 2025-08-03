#include <Servo.h>

Servo myservo;

void setup() {
  myservo.attach(9);  // Connect to pin 9
}

void loop() {
  for (int pos = 0; pos <= 180; pos += 1) {
    myservo.write(pos);
    delay(15);  // wait for servo to reach
  }

  for (int pos = 180; pos >= 0; pos -= 1) {
    myservo.write(pos);
    delay(15);
  }
}

