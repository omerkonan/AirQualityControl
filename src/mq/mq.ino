int MQ2_PIN = A0;     
int MQ4_PIN = A1;     
int MQ6_PIN = A2;     
int MQ7_PIN = A3;     
int MQ8_PIN = A4;     
int MQ135_PIN  =  A5;     

void setup()
{
  Serial.begin(115200);                               
   
 }
 
void loop(){

  int mq2 = analogRead(MQ2_PIN);
  int mq4 = analogRead(MQ4_PIN);
  int mq6 = analogRead(MQ6_PIN);
  int mq7 = analogRead(MQ7_PIN);
  int mq8 = analogRead(MQ8_PIN);
  int mq135 = analogRead(MQ135_PIN);


  Serial.print("mq2:");
  Serial.println(mq2);
  delay(500);
  Serial.print("mq4:");
  Serial.println(mq4);
  delay(500);
  Serial.print("mq6:");
  Serial.println(mq6);
  delay(500);
  Serial.print("mq7:");
  Serial.println(mq7);
  delay(500);
  Serial.print("mq8:");
  Serial.println(mq8);
  delay(500);
  Serial.print("mq135:");
  Serial.println(mq135);
  delay(500);
}
