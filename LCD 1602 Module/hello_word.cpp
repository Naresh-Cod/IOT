#include <LiquidCrystal.h>

// RS, E, D4, D5, D6, D7
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
  lcd.begin(16, 2);           // 16 columns, 2 rows
  lcd.print("Hello, World!"); // Print message
}

void loop() {
  lcd.setCursor(0, 1);         // Set to second line
  lcd.print("LCD 1602 Module");
  delay(1000);
}

