#include <Stepper.h>
 
const int stepsPerRevolution = 800;   // Number of steps (if stepper motor)
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);

int k = 2071.5;
int cou = 0;

void setup()
{
  myStepper.setSpeed(50);             // Setting the velocity  
  Serial.begin(9600);                 
}
 
void loop()
{
   if (Serial.available()) {
    String message = Serial.readString();
    if (message != "") {
      while (1) {
          cou += stepsPerRevolution;      
          myStepper.step(stepsPerRevolution);
          delay(20);      
            if (cou == 7200)
              {
                Serial.print(k * (cou*0.01/200));
                Serial.print(" ");
                Serial.println(cou*0.01/200);
                delay(500);      
                myStepper.step(-cou);  
                cou = 0;
                break;
              }
        }    

    }
  }

}