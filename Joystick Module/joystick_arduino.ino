int VRx = A0;
int VRy = A1;
int SW = 2;

void setup() {
  pinMode(SW, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  int xVal = analogRead(VRx);
  int yVal = analogRead(VRy);
  int btnState = digitalRead(SW);  // LOW = Pressed

  Serial.print(xVal);
  Serial.print(",");
  Serial.print(yVal);
  Serial.print(",");
  Serial.println(btnState);

  delay(100);
}
