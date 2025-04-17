#define MAX_BUFF_LEN 255

char c;
char str[MAX_BUFF_LEN];
uint8_t idx = 0;

#define FLASH_LED_PIN 4

void setup() {
  Serial.begin(115200);
  pinMode(FLASH_LED_PIN, OUTPUT);
  digitalWrite(FLASH_LED_PIN, LOW); // Make sure it's off

}

void loop() {
  //Serial.println("Hello from ESP!");

  if(Serial.available() > 0){
    c = Serial.read(); // Read one byte

//    if(c != '\n'){ // Still reading
//      str[idx++] = c; // Parse the string byte (char) by byte
//    }else{ // Done reading
//      str[idx] ='\0'; // Convert it to a string
//      idx = 0;

    if(c=='1'){
      digitalWrite(FLASH_LED_PIN, HIGH);  // Turn on flash
      Serial.println("FLASH ON");


    }else if (c== '0') {
      digitalWrite(FLASH_LED_PIN, LOW);   // Turn off flash
      Serial.println("FLASH OFF");


//      Serial.print("Received: ");
//      Serial.print(str);
    }
  }
}
