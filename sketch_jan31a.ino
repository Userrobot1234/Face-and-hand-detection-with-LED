int led = 13; // variable int is set as led and GPIO Pin is set as 13
int led2 = 8; // same here,but GPIO is Pin 8

void setup() { 
  pinMode(led, OUTPUT);
  pinMode(led2,OUTPUT);
  Serial.begin(9600);  //serial coomunication b/w thonny and arduino is established
} 
 
void loop() { 
  if (Serial.available()) { 
    char data = Serial.read(); // Char data reads value and stores data on serial
    if (data == '1') 
    {
      digitalWrite(led, HIGH);
      digitalWrite(led2, LOW);
    }  
    else if (data == '0') 
    {
      digitalWrite(led2, HIGH); 
      digitalWrite(led, LOW); 
    }
  } 
}
