int segmentPins[] = {2, 3, 4, 5, 6, 7, 8}; // a, b, c, d, e, f, g
int digitPins[] = {10, 11, 12, 13};        // Digit 1 to 4

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

unsigned long lastUpdate = 0;
int hours = 12, minutes = 0;

void setup()
{
    for (int i = 0; i < 7; i++)
        pinMode(segmentPins[i], OUTPUT);
    for (int i = 0; i < 4; i++)
        pinMode(digitPins[i], OUTPUT);
}

void loop()
{
    // Update time every 60000 ms = 1 minute
    if (millis() - lastUpdate >= 60000)
    {
        lastUpdate = millis();
        minutes++;
        if (minutes >= 60)
        {
            minutes = 0;
            hours++;
            if (hours >= 24)
                hours = 0;
        }
    }

    int displayDigits[4] = {
        hours / 10, hours % 10,
        minutes / 10, minutes % 10};

    // Display each digit briefly (multiplexing)
    for (int i = 0; i < 4; i++)
    {
        displayDigit(displayDigits[i], i);
        delay(5);
    }
}

void displayDigit(int num, int digit)
{
    for (int i = 0; i < 4; i++)
        digitalWrite(digitPins[i], HIGH); // turn off all
    for (int j = 0; j < 7; j++)
        digitalWrite(segmentPins[j], bitRead(digits[num], j));
    digitalWrite(digitPins[digit], LOW); // turn on current digit
}
