
// Husk ESCON(motordriver) bliver reset ved arduino opstart. og såfremt den har en error nustillies denne. Dette gøres af sikerhedshensyn kun ved opstart.

//  PWM to ESCON(motor driver) Scaling
//  duty cycle <10% = invalid, motor driver will shut down
//  duty cycle 10% = -11A
//  duty cycle 50% = 0A
//  duty cycle 90% = +11A
//  duty cycle >90% = invalid, motor driver will shut down
//  PWM = 8bit, 0-255,  127/128 = 50

#include <TimerOne.h>     // remember to install
#include <Encoder.h>

#define PWM_PIN 11

#define ENABLE_PIN 12
//#define POTMETER A0
//#define CURRENT_INPUT A5

// Change these two numbers to the pins connected to your encoder.
//   Best Performance: both pins have interrupt capability
//   Good Performance: only the first pin has interrupt capability
//   Low Performance:  neither pin has interrupt capability
Encoder myEnc(2, 3);
//   avoid using pins with LEDs attached

unsigned long previousMillis = 0;
int squareCount = 0;

const long looptime = 50;  // looptime in ms.
long setpoint = 0;
float pgain = 0.05;
float calcedPWM = 0;

long oldPosition  = -1;

void setup() {
  // put your setup code here, to run once:

  // setup timerOne, we use this library to get 10bit resolution for PWM.
  Timer1.initialize(2000);
  Timer1.stop();        //stop the counter
  Timer1.restart();     //set the clock to zero
  pinMode(PWM_PIN, OUTPUT);
  Timer1.pwm(PWM_PIN, 512, 2000);   // setup to 500Hz and 50% Duty cycle
  // to change PWM use the following function
  //  Timer1.setPwmDuty(PWM_PIN, 512);
  // we setup this pwm signal before enabling the ESCON, så that it gets a valid pwm from the start.

  pinMode(ENABLE_PIN, OUTPUT);
  digitalWrite(ENABLE_PIN, LOW);  // disable ESCON to clear any errors
  delay(2000);
  digitalWrite(ENABLE_PIN, HIGH);  // enable ESCON
  Serial.begin(115200);            // enable serial comm

  previousMillis = millis();    // take initial timestamp.
  //Flush serial
  while (Serial.available() > 0) {
    char t = Serial.read();
  }
}


void loop() {

  long pos = myEnc.read();
  // if (newPosition != oldPosition) {
  //   oldPosition = newPosition;
  //   Serial.println(newPosition);
  //  }


 // Serial.print(pos);
  //Serial.print(" ");
  //Serial.println(millis());

  /*// sqaure wave
    if(squareCount > 2000)
      squareCount = 0;
    else
     squareCount++;
    if(squareCount < 1000)
      setpoint = -10000;
    else
      setpoint = 10000;
  */

  if (Serial.available() > 4) {
    //Serial.print(" read ");
    // read the incoming byte:
    setpoint = Serial.parseInt();
    //setpoint = Serial.read();
    
    //Serial.println(setpoint);
    //Serial.read();
  }
  //Serial.print(",");
  //Serial.println(setpoint);        // print for debug


  // Ren P regulator
  calcedPWM = 512 + ((setpoint - pos) * pgain);


  // limit pwm til valid range
  if (calcedPWM > 916)
    calcedPWM = 916;
  if (calcedPWM < 105)
    calcedPWM = 105;

  //  constrain(calcedPWM, 105, 916);  //limit pwm til valid range

  // invert signal
  calcedPWM = 1024 - calcedPWM;

  //Serial.print(" ,duty: ");
  //Serial.println(calcedPWM);
  Timer1.setPwmDuty(PWM_PIN, calcedPWM);

  // vent til looptime er gået.
  while ((previousMillis + looptime) > millis())
  {} // wait
  previousMillis = millis(); // tak new timestamp
}
