int VRx = A0;
int VRy = A1;
int SW = 2;

void setup() {
  pinMode(SW, INPUT_PULLUP); // switch is LOW when pressed
  Serial.begin(9600);
}

void loop() {
  int xVal = analogRead(VRx);
  int yVal = analogRead(VRy);
  int btnState = digitalRead(SW);

  Serial.print("X: ");
  Serial.print(xVal);
  Serial.print(" | Y: ");
  Serial.print(yVal);
  Serial.print(" | Button: ");
  Serial.println(btnState == LOW ? "Pressed" : "Released");

  delay(200);
}

