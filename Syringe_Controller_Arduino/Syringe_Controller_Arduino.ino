const int dirPin = 4;
const int stepPin = 3;
const int stepsPerRevolution = 480;
int CAsteps, CAspeed;

void setup() {
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  Serial.begin(9600);
  }

void loop() {
  if(Serial.available()>0){
    String command = Serial.readStringUntil('\n');
    command.trim();
    
    if (command.startsWith("8:")) { //Set droplet size
      CAsteps = command.substring(2).toInt();
    }
    else if (command.startsWith("9:")) { //Set dispense speed
      CAspeed = command.substring(2).toInt();
    }
    else if (command == "0") { //Fill the whole syringe
      for(int x = 0; x < stepsPerRevolution; x++)
        {
          digitalWrite(dirPin, LOW);
          digitalWrite(stepPin, HIGH);
          delayMicroseconds(1000);
          digitalWrite(stepPin, LOW);
          delayMicroseconds(1000);
        }
        command = "3";}

      else if(command == "1"){ //Empty the whole syringe
        for(int x = 0; x < stepsPerRevolution; x++)
          {
            digitalWrite(dirPin, HIGH);
            digitalWrite(stepPin, HIGH);
            delayMicroseconds(1000);
            digitalWrite(stepPin, LOW);
            delayMicroseconds(1000);
          }
          command = "3";}


      else if(command == "2"){ //Move the motor for CAsteps at CAspeed (dispense a controlled drop)
        for(int x = 0; x < CAsteps; x++)
            {
            digitalWrite(dirPin, HIGH);
            digitalWrite(stepPin, HIGH);
            delayMicroseconds(CAspeed);
            digitalWrite(stepPin, LOW);
            delayMicroseconds(CAspeed);
           }
         command = "3";}

       else if(command == "3"){} //Stop the motor and do nothing
}}
