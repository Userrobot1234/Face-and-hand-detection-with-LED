int led = 13; 
int led2 = 8;

void setup() { 
  pinMode(led, OUTPUT);
  pinMode(led2,OUTPUT);
  Serial.begin(9600); 
} 
 
void loop() { 
  if (Serial.available()) { 
    char data = Serial.read(); 
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