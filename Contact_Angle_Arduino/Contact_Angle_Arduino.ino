const int dirPin = 4;
const int stepPin = 3;
const int stepsPerRevolution = 480;
char serialData;
int CAsteps, CAspeed, sos2;
String readString, category, sos;

void setup() {
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  Serial.begin(9600);
  }

void loop() {
  if(Serial.available()>0){
     serialData = Serial.read();
     readString += serialData;
     category = readString.substring(0); //reads first char
     sos = readString.substring(1,10); //reads the rest of the char
     sos2 = sos.toInt();
      
      if(category == '0'){
        for(int x = 0; x < stepsPerRevolution; x++)
          {
            digitalWrite(dirPin, LOW);
            digitalWrite(stepPin, LOW);
            delayMicroseconds(1000);
            digitalWrite(stepPin, LOW);
            delayMicroseconds(1000);
          }
          category = '3';}

      else if(category == '1'){
        for(int x = 0; x < stepsPerRevolution; x++)
          {
            digitalWrite(dirPin, HIGH);
            digitalWrite(stepPin, LOW);
            delayMicroseconds(1000);
            digitalWrite(stepPin, LOW);
            delayMicroseconds(1000);
          }
          category = '3';}

      else if(category == '8'){
        CAsteps = sos2;
      category = '3';}

      else if(category == '9'){
        CAspeed = sos2;
      category = '3';}

      else if(category == '2'){
        for(int x = 0; x < CAsteps; x++)
            {
            digitalWrite(dirPin, LOW);
            digitalWrite(stepPin, LOW);
            delayMicroseconds(CAspeed);
            digitalWrite(stepPin, LOW);
            delayMicroseconds(CAspeed);
           }
         category = '3';}

       else if(category == '3'){}
}}
